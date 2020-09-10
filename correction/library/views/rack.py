import datetime
from ..forms.rackform import AddRackForm, EditRackForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import formats
from django.views import View
from ..models import Rack


class AllRackView(View):
    model = Rack
    template_name = 'rack/index.html'

    def get(self, request):
        racks = Rack.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'racks': racks, 'date': date}
        return render(request, self.template_name, context)


class AddRackView(View):
    model = Rack
    form_class = AddRackForm
    template_name = 'rack/add_rack.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            rack = form.save(commit=False)
            rack.save()
            response = {
                'user': rack.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditRackView(View):
    model = Rack
    form_class = EditRackForm
    template_name = 'rack/edit_rack.html'

    def get(self, request, pk, *args, **kwargs):
        rack = Rack.objects.get(pk=pk)
        form = self.form_class(instance=rack)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        rack = Rack.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=rack)

        if form.is_valid():
            form.save()

            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteRackView(View):

    template_name = 'rack/delete_rack.html'

    def get(self, request, pk):
        rack = Rack.objects.get(pk=pk)
        context = {
            'rack': rack
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        rack = Rack.objects.get(pk=pk)
        rack.active_status = 0
        rack.save()
        return redirect('library:racks')


class DetailRackView(View):
    def get(self, request, pk):
        rack = Rack.objects.get(pk=pk)
        context = {
            'rack': rack
        }
        return render(request, 'rack/detail_rack.html', context)







from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from ..models import Postaldispatch
from ..forms.postaldispatchform import AddPostaldispatchForm, EditPostaldispatchForm
import datetime
from django.utils import formats


class AllPostalDispatchView(View):
    model = Postaldispatch
    template_name = 'postaldispatch/index.html'

    def get(self, request):
        postaldispatchs = Postaldispatch.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'postaldispatchs': postaldispatchs, 'date': date}
        return render(request, self.template_name, context)


class AddPostalDispatchView(View):
    model = Postaldispatch
    form_class = AddPostaldispatchForm
    template_name = 'postaldispatch/add_postaldispatch.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            postaldispatch = form.save(commit=False)
            postaldispatch.save()
            response = {
                'user': postaldispatch.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditPostalDispatchView(View):
    model = Postaldispatch
    form_class = EditPostaldispatchForm
    template_name = 'postaldispatch/edit_postaldispatch.html'

    def get(self, request, pk, *args, **kwargs):
        postaldispatch = Postaldispatch.objects.get(pk=pk)
        form = self.form_class(instance=postaldispatch)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        postaldispatch = Postaldispatch.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=postaldispatch)

        if form.is_valid():
            form.save()
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeletePostalDispatchView(View):
    template_name = 'postaldispatch/delete_postaldispatch.html'

    def get(self, request, pk):
        postaldispatch = Postaldispatch.objects.get(pk=pk)
        context = {
            'postaldispatch': postaldispatch
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        postaldispatch = Postaldispatch.objects.get(pk=pk)
        postaldispatch.active_status = 0
        postaldispatch.save()

        return redirect('frontoffice:postaldispatchs')


class DetailPostalDispatchView(View):
    pass
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from ..models import Visitorbook
from ..forms.visitorbookform import AddVisitorbookForm, EditVisitorbookForm
import datetime
from django.utils import formats


class AllVisitorBookView(View):
    model = Visitorbook
    template_name = 'visitorbook/index.html'

    def get(self, request):
        visitorbooks = Visitorbook.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'visitorbooks': visitorbooks, 'date': date}
        return render(request, self.template_name, context)


class AddVisitorBookView(View):
    model = Visitorbook
    form_class = AddVisitorbookForm
    template_name = 'visitorbook/add_visitorbook.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            visitorbook = form.save(commit=False)
            visitorbook.save()
            response = {
                'user': visitorbook.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditVisitorBookView(View):
    model = Visitorbook
    form_class = EditVisitorbookForm
    template_name = 'visitorbook/edit_visitorbook.html'

    def get(self, request, pk, *args, **kwargs):
        visitorbook = Visitorbook.objects.get(pk=pk)
        form = self.form_class(instance=visitorbook)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        visitorbook = Visitorbook.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=visitorbook)

        if form.is_valid():
            form.save()
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteVisitorBookView(View):
    template_name = 'visitorbook/delete_visitorbook.html'

    def get(self, request, pk):
        visitorbook = Visitorbook.objects.get(pk=pk)
        context = {
            'visitorbook': visitorbook
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        visitorbook = Visitorbook.objects.get(pk=pk)
        visitorbook.active_status = 0
        visitorbook.save()
        return redirect('frontoffice:visitorbooks')


class DetailVisitorBookView(View):
    pass
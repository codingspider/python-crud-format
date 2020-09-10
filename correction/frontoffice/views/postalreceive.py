from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from ..models import Postalreceive
from ..forms.postalreceiveform import AddPostalreceiveForm, EditPostalreceiveForm
import datetime
from django.utils import formats


class AllPostalReceiveView(View):
    model = Postalreceive
    template_name = 'postalreceive/index.html'

    def get(self, request):
        postalreceives = Postalreceive.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'postalreceives': postalreceives, 'date': date}
        return render(request, self.template_name, context)


class AddPostalReceiveView(View):
    model = Postalreceive
    form_class = AddPostalreceiveForm
    template_name = 'postalreceive/add_postalreceive.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            postalreceive = form.save(commit=False)
            postalreceive.save()
            response = {
                'user': postalreceive.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditPostalReceiveView(View):
    model = Postalreceive
    form_class = EditPostalreceiveForm
    template_name = 'postalreceive/edit_postalreceive.html'

    def get(self, request, pk, *args, **kwargs):
        postalreceive = Postalreceive.objects.get(pk=pk)
        form = self.form_class(instance=postalreceive)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        postalreceive = Postalreceive.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=postalreceive)

        if form.is_valid():
            form.save()
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeletePostalReceiveView(View):
    template_name = 'postalreceive/delete_postalreceive.html'

    def get(self, request, pk):
        postalreceive = Postalreceive.objects.get(pk=pk)
        context = {
            'postalreceive': postalreceive
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        postaldispatch = Postalreceive.objects.get(pk=pk)
        postaldispatch.active_status = 0
        postaldispatch.save()
        return redirect('frontoffice:postalreceives')


class DetailPostalReceiveView(View):
    pass
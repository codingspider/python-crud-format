from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from ..models import Postalreceive
from ..forms.forms import PostalreceiveForm
import datetime
from django.utils import formats


class AllPostalReceiveView(View):
    model = Postalreceive
    template_name = 'postalreceive/index.html'

    def get(self, request):
        postal_receive = Postalreceive.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'postal_receive': postal_receive, 'date': date}
        return render(request, self.template_name, context)


class AddPostalReceiveView(View):
    model = Postalreceive
    form_class = PostalreceiveForm
    template_name = 'postalreceive/add_postal_receive.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            postal_receive = form.save(commit=False)
            postal_receive.save()
            response = {
                'user': postal_receive.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditPostalReceiveView(View):
    model = Postalreceive
    form_class = PostalreceiveForm
    template_name = 'postalreceive/edit_postal_receive.html'

    def get(self, request, pk, *args, **kwargs):
        postal_receive = Postalreceive.objects.get(pk=pk)
        form = self.form_class(instance=postal_receive)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        notices = Postalreceive.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=notices)

        if form.is_valid():
            form.save()
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeletePostalReceiveView(View):
    template_name = 'postalreceive/delete_postal_receive.html'

    def get(self, request, pk):
        complain = Postalreceive.objects.get(pk=pk)
        context = {
            'complain': complain
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        postal_dispatch = Postalreceive.objects.get(pk=pk)
        postal_dispatch.active_status = 0
        postal_dispatch.save()
        return redirect('frontoffice:postalreceives')


class DetailPostalReceiveView(View):
    pass
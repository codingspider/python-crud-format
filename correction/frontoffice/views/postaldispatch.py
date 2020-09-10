from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from ..models import Postaldispatch
from ..forms.forms import PostaldispatchForm
import datetime
from django.utils import formats


class AllPostalDispatchView(View):
    model = Postaldispatch
    template_name = 'postaldispatch/index.html'

    def get(self, request):
        postal_dispatch = Postaldispatch.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'postal_dispatch': postal_dispatch, 'date': date}
        return render(request, self.template_name, context)


class AddPostalDispatchView(View):
    model = Postaldispatch
    form_class = PostaldispatchForm
    template_name = 'postaldispatch/add_postal_dispatch.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            postal_dispatch = form.save(commit=False)
            postal_dispatch.save()
            response = {
                'user': postal_dispatch.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditPostalDispatchView(View):
    model = Postaldispatch
    form_class = PostaldispatchForm
    template_name = 'postaldispatch/edit_postal_dispatch.html'

    def get(self, request, pk, *args, **kwargs):
        postal_dispatch = Postaldispatch.objects.get(pk=pk)
        form = self.form_class(instance=postal_dispatch)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        notices = Postaldispatch.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=notices)

        if form.is_valid():
            form.save()
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeletePostalDispatchView(View):
    template_name = 'postaldispatch/delete_postal_dispatch.html'

    def get(self, request, pk):
        complain = Postaldispatch.objects.get(pk=pk)
        context = {
            'complain': complain
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        postal_dispatch = Postaldispatch.objects.get(pk=pk)
        postal_dispatch.active_status = 0
        postal_dispatch.save()

        return redirect('frontoffice:postaldispatchs')


class DetailPostalDispatchView(View):
    pass
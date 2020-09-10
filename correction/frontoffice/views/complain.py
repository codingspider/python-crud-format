from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from ..models import Complain
from ..forms.forms import ComplainForm
import datetime
from django.utils import formats


class AllComplainView(View):
    model = Complain
    template_name = 'complain/index.html'

    def get(self, request):
        complains = Complain.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'complains': complains, 'date': date}
        return render(request, self.template_name, context)


class AddComplainView(View):
    model = Complain
    form_class = ComplainForm
    template_name = 'complain/add_complain.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            conplain = form.save(commit=False)
            conplain.save()

            response = {
                'user': conplain.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditComplainView(View):
    model = Complain
    form_class = ComplainForm
    template_name = 'complain/edit_complain.html'

    def get(self, request, pk, *args, **kwargs):
        notices = Complain.objects.get(pk=pk)
        form = self.form_class(instance=notices)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        notices = Complain.objects.get(pk=pk)
        form = self.form_class(request.POST,request.FILES, instance=notices)

        if form.is_valid():
            form.save()

            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteComplainView(View):

    template_name = 'complain/delete_complain.html'

    def get(self, request, pk):
        complain = Complain.objects.get(pk=pk)
        context ={
            'complain': complain
        }
        return render(request, self.template_name,context)

    def post(self, request, pk, *args, **kwargs):
        notice = Complain.objects.get(pk=pk)
        notice.active_status = 0
        notice.save()

        return redirect('frontoffice:complains')


class DetailComplainView(View):
    pass
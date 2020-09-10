from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from ..models import Visitorbook
from ..forms.forms import VisitorbookForm
import datetime
from django.utils import formats


class AllVisitorBookView(View):
    model = Visitorbook
    template_name = 'visitorbook/index.html'

    def get(self, request):
        visitor_book = Visitorbook.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'visitor_book': visitor_book, 'date': date}
        return render(request, self.template_name, context)


class AddVisitorBookView(View):
    model = Visitorbook
    form_class = VisitorbookForm
    template_name = 'visitorbook/add_visitor_book.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            visitor_book = form.save(commit=False)
            visitor_book.save()
            response = {
                'user': visitor_book.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditVisitorBookView(View):
    model = Visitorbook
    form_class = VisitorbookForm
    template_name = 'visitorbook/edit_visitor_book.html'

    def get(self, request, pk, *args, **kwargs):
        postal_receive = Visitorbook.objects.get(pk=pk)
        form = self.form_class(instance=postal_receive)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        visitor = Visitorbook.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=visitor)

        if form.is_valid():
            form.save()
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteVisitorBookView(View):
    template_name = 'visitorbook/delete_visitor_book.html'

    def get(self, request, pk):
        visitor = Visitorbook.objects.get(pk=pk)
        context = {
            'visitor': visitor
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        postal_dispatch = Visitorbook.objects.get(pk=pk)
        postal_dispatch.active_status = 0
        postal_dispatch.save()
        return redirect('frontoffice:visitorbooks')


class DetailVisitorBookView(View):
    pass
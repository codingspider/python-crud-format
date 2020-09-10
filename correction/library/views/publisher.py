import datetime
from ..forms.publisherform import AddPublisherForm, EditPublisherForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import formats
from django.views import View
from ..models import Publisher


class AllPublisherView(View):
    model = Publisher
    template_name = 'publisher/index.html'

    def get(self, request):
        publishers = Publisher.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'publishers': publishers, 'date': date}
        return render(request, self.template_name, context)


class AddPublisherView(View):
    model = Publisher
    form_class = AddPublisherForm
    template_name = 'publisher/add_publisher.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            publisher = form.save(commit=False)
            publisher.save()
            response = {
                'user': publisher.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditPublisherView(View):
    model = Publisher
    form_class = EditPublisherForm
    template_name = 'publisher/edit_publisher.html'

    def get(self, request, pk, *args, **kwargs):
        publisher = Publisher.objects.get(pk=pk)
        form = self.form_class(instance=publisher)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        publisher = Publisher.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=publisher)

        if form.is_valid():
            form.save()

            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeletePublisherView(View):

    template_name = 'publisher/delete_publisher.html'

    def get(self, request, pk):
        publisher = Publisher.objects.get(pk=pk)
        context = {
            'publisher': publisher
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        publisher = Publisher.objects.get(pk=pk)
        publisher.active_status = 0
        publisher.save()
        return redirect('library:publishers')


class DetailPublisherView(View):
    def get(self, request, pk):
        publisher = Publisher.objects.get(pk=pk)
        context = {
            'publisher': publisher
        }
        return render(request, 'publisher/detail_publisher.html', context)







import datetime
from ..forms.ebookform import AddEBookForm, EditEBookForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import formats
from django.views import View
from ..models import EBook
from django.http import HttpResponse


class AllEbookView(View):
    model = EBook
    template_name = 'ebook/index.html'

    def get(self, request):
        ebooks = EBook.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'ebooks': ebooks, 'date': date}
        return render(request, self.template_name, context)


class AddEbookView(View):
    model = EBook
    form_class = AddEBookForm
    template_name = 'ebook/add_ebook.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            response = {
                'user': book.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditEbookView(View):
    model = EBook
    form_class = EditEBookForm
    template_name = 'ebook/edit_ebook.html'

    def get(self, request, pk, *args, **kwargs):
        ebook = EBook.objects.get(pk=pk)
        form = self.form_class(instance=ebook)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        ebook = EBook.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=ebook)

        if form.is_valid():
            form.save()

            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteEbookView(View):

    template_name = 'ebook/delete_ebook.html'

    def get(self, request, pk):
        ebook = EBook.objects.get(pk=pk)
        context = {
            'ebook': ebook
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        ebook = EBook.objects.get(pk=pk)
        ebook.active_status = 0
        ebook.save()
        return redirect('library:ebooks')


class DetailEbookView(View):
    def get(self, request, pk):
        ebook = EBook.objects.get(pk=pk)
        context = {
            'ebook': ebook
        }
        return render(request, 'ebook/detail_ebook.html', context)







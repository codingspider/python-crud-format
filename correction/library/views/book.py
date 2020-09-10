import datetime
from ..forms.bookform import AddBookForm, EditBookForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import formats
from django.views import View
from ..models import Book
from django.http import HttpResponse


class AllBookView(View):
    model = Book
    template_name = 'book/index.html'

    def get(self, request):
        books = Book.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'books': books, 'date': date}
        return render(request, self.template_name, context)


class AddBookView(View):
    model = Book
    form_class = AddBookForm
    template_name = 'book/add_book.html'

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


class EditBookView(View):
    model = Book
    form_class = EditBookForm
    template_name = 'book/edit_book.html'

    def get(self, request, pk, *args, **kwargs):
        book = Book.objects.get(pk=pk)
        form = self.form_class(instance=book)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        book = Book.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()

            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteBookView(View):

    template_name = 'book/delete_book.html'

    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        context = {
            'book': book
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        book = Book.objects.get(pk=pk)
        book.active_status = 0
        book.save()
        return redirect('library:books')


class DetailBookView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        context = {
            'book': book
        }
        return render(request, 'book/detail_book.html', context)







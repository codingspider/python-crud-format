import datetime
from ..forms.authorform import AddAuthorForm, EditAuthorForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import formats
from django.views import View
from ..models import Author


class AllAuthorView(View):
    model = Author
    template_name = 'author/index.html'

    def get(self, request):
        authors = Author.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'authors': authors, 'date': date}
        return render(request, self.template_name, context)


class AddAuthorView(View):
    model = Author
    form_class = AddAuthorForm
    template_name = 'author/add_author.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            response = {
                'user': author.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditAuthorView(View):
    model = Author
    form_class = EditAuthorForm
    template_name = 'author/edit_author.html'

    def get(self, request, pk, *args, **kwargs):
        author = Author.objects.get(pk=pk)
        form = self.form_class(instance=author)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        authors = Author.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=authors)

        if form.is_valid():
            form.save()

            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteAuthorView(View):

    template_name = 'author/delete_author.html'

    def get(self, request, pk):
        author = Author.objects.get(pk=pk)
        context = {
            'author': author
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        author = Author.objects.get(pk=pk)
        author.active_status = 0
        author.save()
        return redirect('library:authors')


class DetailAuthorView(View):
    def get(self, request, pk):
        author = Author.objects.get(pk=pk)
        context = {
            'author': author
        }
        return render(request, 'author/detail_author.html', context)







import datetime
from ..forms.booklanguageform import AddBookLanguageForm, EditBookLanguageForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import formats
from django.views import View
from ..models import BookLanguage


class AllBookLanguageView(View):
    model = BookLanguage
    template_name = 'booklanguage/index.html'

    def get(self, request):
        booklanguages = BookLanguage.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'booklanguages': booklanguages, 'date': date}
        return render(request, self.template_name, context)


class AddBookLanguageView(View):
    model = BookLanguage
    form_class = AddBookLanguageForm
    template_name = 'booklanguage/add_booklanguage.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            booklanguage = form.save(commit=False)
            booklanguage.save()
            response = {
                'user': booklanguage.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditBookLanguageView(View):
    model = BookLanguage
    form_class = EditBookLanguageForm
    template_name = 'booklanguage/edit_booklanguage.html'

    def get(self, request, pk, *args, **kwargs):
        booklanguage = BookLanguage.objects.get(pk=pk)
        form = self.form_class(instance=booklanguage)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        booklanguage = BookLanguage.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=booklanguage)

        if form.is_valid():
            form.save()
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteBookLanguageView(View):

    template_name = 'booklanguage/delete_booklanguage.html'

    def get(self, request, pk):
        booklanguage = BookLanguage.objects.get(pk=pk)
        context = {
            'booklanguage': booklanguage
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        booklanguage = BookLanguage.objects.get(pk=pk)
        booklanguage.active_status = 0
        booklanguage.save()
        return redirect('library:booklanguages')


class DetailBookLanguageView(View):
   pass


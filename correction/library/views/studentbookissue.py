import datetime
from ..forms.bookissueform import AddStudentBookIssueForm, EditStudentBookIssueForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import formats
from django.views import View
from ..models import BookIssue


class AllBookIssueView(View):
    model = BookIssue
    template_name = 'bookissue/index.html'

    def get(self, request):
        bookissues = BookIssue.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'bookissues': bookissues, 'date': date}
        return render(request, self.template_name, context)


class AddBookIssueView(View):
    model = BookIssue
    form_class = AddStudentBookIssueForm
    template_name = 'studentbookissue/add_studentbookissue.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            bookissue = form.save(commit=False)
            bookissue.save()
            response = {
                'user': bookissue.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditBookIssueView(View):
    model = BookIssue
    form_class = EditStudentBookIssueForm
    template_name = 'bookissue/edit_bookissue.html'

    def get(self, request, pk, *args, **kwargs):
        bookissue = BookIssue.objects.get(pk=pk)
        form = self.form_class(instance=bookissue)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        rack = BookIssue.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=rack)

        if form.is_valid():
            form.save()

            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteBookIssueView(View):

    template_name = 'bookissue/delete_bookissue.html'

    def get(self, request, pk):
        bookissue = BookIssue.objects.get(pk=pk)
        context = {
            'bookissue': bookissue
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        bookissue = BookIssue.objects.get(pk=pk)
        bookissue.active_status = 0
        bookissue.save()
        return redirect('library:racks')


class DetailBookIssueView(View):
    def get(self, request, pk):
        bookissue = BookIssue.objects.get(pk=pk)
        context = {
            'bookissue': bookissue
        }
        return render(request, 'bookissue/detail_bookissue.html', context)







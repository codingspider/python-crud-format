import datetime
from ..forms.subjectform import AddSubjectForm, EditSubjectForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import formats
from django.views import View
from ..models import Subject


class AllSubjectView(View):
    model = Subject
    template_name = 'subject/index.html'

    def get(self, request):
        subjects = Subject.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'subjects': subjects, 'date': date}
        return render(request, self.template_name, context)


class AddSubjectView(View):
    model = Subject
    form_class = AddSubjectForm
    template_name = 'subject/add_subject.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()
            response = {
                'user': subject.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditSubjectView(View):
    model = Subject
    form_class = EditSubjectForm
    template_name = 'subject/edit_subject.html'

    def get(self, request, pk, *args, **kwargs):
        subject = Subject.objects.get(pk=pk)
        form = self.form_class(instance=subject)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        subject = Subject.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=subject)

        if form.is_valid():
            form.save()

            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteSubjectView(View):

    template_name = 'subject/delete_subject.html'

    def get(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        context = {
            'subject': subject
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        subject = Subject.objects.get(pk=pk)
        subject.active_status = 0
        subject.save()
        return redirect('library:publishers')


class DetailSubjectView(View):
    def get(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        context = {
            'subject': subject
        }
        return render(request, 'subject/detail_subject.html', context)







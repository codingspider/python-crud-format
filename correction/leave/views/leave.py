import datetime
from ..forms.leaveform import AddLeaveForm, EditLeaveForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import formats
from django.views import View
from ..models import Leave, LeaveType


class AllLeaveView(View):
    model = Leave
    template_name = 'leave/index.html'

    def get(self, request):
        leaves = Leave.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'leaves': leaves, 'date': date}
        return render(request, self.template_name, context)


class AddLeaveView(View):
    model = Leave
    form_class = AddLeaveForm
    template_name = 'leave/add_leave.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.save()
            response = {
                'user': leave.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditLeaveView(View):
    model = Leave
    form_class = EditLeaveForm
    template_name = 'leave/edit_leave.html'

    def get(self, request, pk, *args, **kwargs):
        leaves = Leave.objects.get(pk=pk)
        form = self.form_class(instance=leaves)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        leaves = Leave.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=leaves)

        if form.is_valid():
            form.save()

            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteLeaveView(View):

    template_name = 'leave/delete_leave.html'

    def get(self, request, pk):
        leaves = Leave.objects.get(pk=pk)
        context = {
            'leaves': leaves
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        leave = Leave.objects.get(pk=pk)
        leave.active_status = 0
        leave.save()
        return redirect('leave:leaves')


class DetailLeaveView(View):
    pass







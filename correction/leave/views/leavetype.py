import datetime
from ..forms.leavetypeform import AddLeaveTypeForm, EditLeaveTypeForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import formats
from django.views import View
from ..models import LeaveType


class AllLeaveTypeView(View):
    model = LeaveType
    template_name = 'leavetype/index.html'

    def get(self, request):
        leave_types = LeaveType.objects.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'leave_types': leave_types, 'date': date}
        return render(request, self.template_name, context)


class AddLeaveTypeView(View):
    model = LeaveType
    form_class = AddLeaveTypeForm
    template_name = 'leavetype/add_leave_type.html'

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


class EditLeaveTypeView(View):
    model = LeaveType
    form_class = EditLeaveTypeForm
    template_name = 'leavetype/edit_leave_type.html'

    def get(self, request, pk, *args, **kwargs):
        leaves = LeaveType.objects.get(pk=pk)
        form = self.form_class(instance=leaves)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        leaves = LeaveType.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=leaves)

        if form.is_valid():
            form.save()

            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteLeaveTypeView(View):

    template_name = 'leavetype/delete_leave_type.html'

    def get(self, request, pk):
        leaves = LeaveType.objects.get(pk=pk)
        context = {
            'leaves': leaves
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        leave = LeaveType.objects.get(pk=pk)
        leave.active_status = 0
        leave.save()
        return redirect('leave:leavetypes')


class DetailLeaveTypeView(View):
    pass







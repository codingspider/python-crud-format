from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from ..models import LeaveType


class AddLeaveTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddLeaveTypeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = LeaveType
        fields = "__all__"
        exclude = ('active_status',)
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),

        }


class EditLeaveTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditLeaveTypeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = LeaveType
        fields = "__all__"
        exclude = ('active_status',)
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),

        }

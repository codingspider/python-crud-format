from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from ..models import Leave, LeaveType


class AddLeaveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(AddLeaveForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['attachment'].widget.attrs.update({'class': ''})

    class Meta:
        model= Leave
        fields = "__all__"
        exclude = ('active_status',)
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'apply_date': DatePickerInput(format='%d-%m-%Y'),
            'from_date': DatePickerInput(format='%d-%m-%Y'),
            'to_date': DatePickerInput(format='%d-%m-%Y'),
        }


class EditLeaveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(EditLeaveForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['attachment'].widget.attrs.update({'class': ''})

    class Meta:
        model= Leave
        fields = "__all__"
        exclude = ('active_status',)
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'apply_date': DatePickerInput(format='%d-%m-%Y'),
            'from_date': DatePickerInput(format='%d-%m-%Y'),
            'to_date': DatePickerInput(format='%d-%m-%Y'),
        }

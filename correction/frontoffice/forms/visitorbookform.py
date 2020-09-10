from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from ..models import *


class AddVisitorbookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddVisitorbookForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['meet_user'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Visitorbook
        fields = '__all__'
        widgets = {
                'note': forms.Textarea(attrs={'rows': 5}),
                'date': DatePickerInput(format='%d-%m-%Y'),
                'in_time': TimePickerInput(format='%I:%M %p'),
                'out_time': TimePickerInput(format='%I:%M %p'),
            }


class EditVisitorbookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditVisitorbookForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['meet_user'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Visitorbook
        fields = '__all__'
        widgets = {
                'note': forms.Textarea(attrs={'rows': 5}),
                'date': DatePickerInput(format='%d-%m-%Y'),
                'in_time': TimePickerInput(format='%I:%M %p'),
                'out_time': TimePickerInput(format='%I:%M %p'),
            }







from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from ..models import *


class AddComplainForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddComplainForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['complain_type'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['complain_by'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['assigned'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Complain
        fields = '__all__'
        widgets = {
                'description': forms.Textarea(attrs={'rows': 5}),
                'note': forms.Textarea(attrs={'rows': 5}),
                'action_taken': forms.Textarea(attrs={'rows': 5}),
                'date': DatePickerInput(format='%d-%m-%Y'),
            }


class EditComplainForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditComplainForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['complain_type'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['complain_by'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['assigned'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Complain
        fields = '__all__'
        widgets = {
                'description': forms.Textarea(attrs={'rows': 5}),
                'note': forms.Textarea(attrs={'rows': 5}),
                'action_taken': forms.Textarea(attrs={'rows': 5}),
                'date': DatePickerInput(format='%d-%m-%Y'),
            }

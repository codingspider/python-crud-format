from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from ..models import *


# ---------------------publisher------------------------------

class AddPublisherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddPublisherForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Publisher
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
        }


class EditPublisherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditPublisherForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Publisher
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
        }


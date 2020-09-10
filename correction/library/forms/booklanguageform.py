from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from ..models import *


class AddBookLanguageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddBookLanguageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = BookLanguage
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }


class EditBookLanguageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditBookLanguageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = BookLanguage
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

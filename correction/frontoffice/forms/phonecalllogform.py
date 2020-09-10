from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from ..models import *


class AddPhonecalllogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddPhonecalllogForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Phonecalllog
        fields = '__all__'
        widgets = {
                'description': forms.Textarea(attrs={'rows': 5}),
                'note': forms.Textarea(attrs={'rows': 5}),
                'date': DatePickerInput(format='%d-%m-%Y'),
                'followup': DatePickerInput(format='%d-%m-%Y'),
            }


class EditPhonecalllogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditPhonecalllogForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Phonecalllog
        fields = '__all__'
        widgets = {
                'description': forms.Textarea(attrs={'rows': 5}),
                'note': forms.Textarea(attrs={'rows': 5}),
                'date': DatePickerInput(format='%d-%m-%Y'),
                'followup': DatePickerInput(format='%d-%m-%Y'),
            }
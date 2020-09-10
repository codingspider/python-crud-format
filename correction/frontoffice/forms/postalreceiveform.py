from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from ..models import *


class AddPostalreceiveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddPostalreceiveForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Postalreceive
        fields = '__all__'
        widgets = {
                'address': forms.Textarea(attrs={'rows': 5}),
                'note': forms.Textarea(attrs={'rows': 5}),
                'receive_date': DatePickerInput(format='%d-%m-%Y'),
            }


class EditPostalreceiveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditPostalreceiveForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Postalreceive
        fields = '__all__'
        widgets = {
                'address': forms.Textarea(attrs={'rows': 5}),
                'note': forms.Textarea(attrs={'rows': 5}),
                'receive_date': DatePickerInput(format='%d-%m-%Y'),
            }

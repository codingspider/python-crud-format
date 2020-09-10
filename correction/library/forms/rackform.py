from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from ..models import *


class AddRackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddRackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Rack
        fields = '__all__'


class EditRackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditRackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Rack
        fields = '__all__'


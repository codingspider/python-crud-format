from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from ..models import *


class VisitorbookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VisitorbookForm, self).__init__(*args, **kwargs)
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


class PhonecalllogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PhonecalllogForm, self).__init__(*args, **kwargs)
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


class PostaldispatchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostaldispatchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = Postaldispatch
        fields = '__all__'
        widgets = {
                'address': forms.Textarea(attrs={'rows': 5}),
                'note': forms.Textarea(attrs={'rows': 5}),
                'dispatch_date': DatePickerInput(format='%d-%m-%Y'),
            }


class PostalreceiveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostalreceiveForm, self).__init__(*args, **kwargs)
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


class ComplainForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComplainForm, self).__init__(*args, **kwargs)
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


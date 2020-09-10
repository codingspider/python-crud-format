from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from ..models import *


class AddBookIssueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddBookIssueForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['member'].widget.attrs.update({'class': 'form-control select2'})
            # self.fields['issue_date'].widget.attrs.update({'class': 'form-control'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = BookIssue
        fields = '__all__'

        widgets = {
            'note': forms.Textarea(attrs={'rows': 5}),
            'issue_date': DatePickerInput(format='%Y-%m-%d'),
            'return_date': DatePickerInput(format='%Y-%m-%d'),
        }


class EditBookIssueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditBookIssueForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['member'].widget.attrs.update({'class': 'form-control select2'})
            # self.fields['issue_date'].widget.attrs.update({'class': 'form-control'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    class Meta:
        model = BookIssue
        fields = '__all__'

        widgets = {
            'note': forms.Textarea(attrs={'rows': 5}),
            'issue_date': DatePickerInput(format='%Y-%m-%d'),
            'return_date': DatePickerInput(format='%Y-%m-%d'),
        }
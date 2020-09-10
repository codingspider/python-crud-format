from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from ..models import *


class AddEBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddEBookForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
            self.fields['author'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['publisher'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['book_language'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['subject'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    # image = ImageField(widget=PictureWidget)
    class Meta:
        model = EBook
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'post_date': DatePickerInput(format='%Y-%m-%d'),
        }


class EditEBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditEBookForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
            self.fields['author'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['publisher'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['book_language'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['subject'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'

    # image = ImageField(widget=PictureWidget)
    class Meta:
        model = EBook
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'post_date': DatePickerInput(format='%Y-%m-%d'),
        }


from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from ..models import IdCard


class IdCardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(IdCardForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = IdCard
        fields = "__all__"
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'valid_till': DatePickerInput(format='%d-%m-%Y'),

        }


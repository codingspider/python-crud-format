from django import forms
from ..models import StudentIdCard


class AddStudentIdForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(AddStudentIdForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = StudentIdCard
        fields = "__all__"
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),

        }


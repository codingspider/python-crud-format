from django import forms

from .models import Teacher


class TeacherForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Teacher
        fields = '__all__'






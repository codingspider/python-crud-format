from django import forms
from ..models import CertificateType


class AddCertificateTypeform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddCertificateTypeform, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CertificateType
        fields = "__all__"
        widgets = {
            'note': forms.Textarea(attrs={'rows': 3}),
            'certificate_text': forms.Textarea(attrs={'rows': 3}),
        }


class EditCertificateTypeform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditCertificateTypeform, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CertificateType
        fields = "__all__"
        widgets = {
            'note': forms.Textarea(attrs={'rows': 3}),
            'certificate_text': forms.Textarea(attrs={'rows': 3}),
        }

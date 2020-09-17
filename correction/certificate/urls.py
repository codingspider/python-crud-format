from django.urls import path
from .views import certificatetype, certificate


app_name = 'certificate'

urlpatterns = [
    # certificate type
    path('certificatetypes/', certificatetype.AllCertificateTypeView.as_view(), name="certificatetypes"),
    path('add_certificatetype/', certificatetype.AddCertificateTypeView.as_view(), name="add_certificatetype"),
    path('edit_certificatetype/<int:pk>', certificatetype.EditCertificateTypeView.as_view(), name="edit_certificatetype"),
    path('delete_certificatetype/<int:pk>', certificatetype.DeleteCertificateTypeView.as_view(), name="delete_certificatetype"),

    path('certificates/', certificate.AllCertificateView.as_view(), name="certificates"),
    path('get_students/', certificate.AllStudentGetView.as_view(), name="get_students"),
    path('generate_certificate/<int:pk>/<int:types>', certificate.GenerateCertificateView.as_view(), name="generate_certificate"),
]

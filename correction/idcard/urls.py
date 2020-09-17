from django.urls import path
from .views import studentidcard, idcard

app_name = 'idcard'

urlpatterns = [
    # complain
    path('studentidcards/', studentidcard.AllStudentIdCardView.as_view(), name="studentidcards"),
    path('add_idcard/', idcard.AddIdCardView.as_view(), name="add_idcard"),
    path('add_studentidcard/', studentidcard.AddStudentIdCardView.as_view(), name="add_studentidcard"),
]







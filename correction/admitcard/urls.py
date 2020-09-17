from django.urls import path
from .views import admitcard

app_name = 'admitcard'

urlpatterns = [
    # complain
    path('add_admitcard/', admitcard.AddAdmitCardView.as_view(), name="add_admitcard"),

]







from django.urls import path
from .views import leave

app_name = 'leave'

urlpatterns = [
    # leave
    path('leaves/', leave.AllLeaveView.as_view(), name="leaves"),
    path('leave/<int:pk>', leave.DetailLeaveView.as_view(), name="leave"),
    path('add_leave/', leave.AddLeaveView.as_view(), name="add_leave"),
    path('edit_leave/<int:pk>', leave.EditLeaveView.as_view(), name="edit_leave"),
    path('delete_leave/<int:pk>', leave.DeleteLeaveView.as_view(), name="delete_leave"),

]







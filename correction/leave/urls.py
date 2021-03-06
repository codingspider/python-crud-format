from django.urls import path
from .views import leavetype, leave

app_name = 'leave'

urlpatterns = [
    # leave
    path('leaves/', leave.AllLeaveView.as_view(), name="leaves"),
    path('leave/<int:pk>', leave.DetailLeaveView.as_view(), name="leave"),
    path('add_leave/', leave.AddLeaveView.as_view(), name="add_leave"),
    path('edit_leave/<int:pk>', leave.EditLeaveView.as_view(), name="edit_leave"),
    path('delete_leave/<int:pk>', leave.DeleteLeaveView.as_view(), name="delete_leave"),

    # leave
    path('leavetypes/', leavetype.AllLeaveTypeView.as_view(), name="leavetypes"),
    path('leavetype/<int:pk>', leavetype.DetailLeaveTypeView.as_view(), name="leavetype"),
    path('add_leave_type/', leavetype.AddLeaveTypeView.as_view(), name="add_leave_type"),
    path('edit_leave_type/<int:pk>', leavetype.EditLeaveTypeView.as_view(), name="edit_leave_type"),
    path('delete_leave_type/<int:pk>', leavetype.DeleteLeaveTypeView.as_view(), name="delete_leave_type"),

]







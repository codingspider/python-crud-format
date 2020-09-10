from django.urls import path

from .views import institute

app_name = "institute"
urlpatterns = [
    path('institutes', institute.AllInstituteView.as_view(), name='institutes'),
    # path('notice/<int:pk>', views.DetailInstituteView.as_view(), name="notice"),
    # path('add_notice/', views.AddInstituteView.as_view(), name="add_notice"),
    # path('edit_notice/<int:pk>', views.EditNoticeView.as_view(), name="edit_notice"),
    # path('delete_notice/<int:pk>', views.DeleteInstituteView.as_view(), name="delete_notice"),

]

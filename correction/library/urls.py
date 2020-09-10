from django.urls import path
from .views import author, publisher, subject

app_name = 'library'

urlpatterns = [
    # Author
    path('authors/', author.AllAuthorView.as_view(), name="authors"),
    path('author_detail/<int:pk>', author.DetailAuthorView.as_view(), name="author_detail"),
    path('add_author/', author.AddAuthorView.as_view(), name="add_author"),
    path('edit_author/<int:pk>', author.EditAuthorView.as_view(), name="edit_author"),
    path('delete_author/<int:pk>', author.DeleteAuthorView.as_view(), name="delete_author"),

    # Publisher
    path('publishers/', publisher.AllPublisherView.as_view(), name="publishers"),
    path('publisher/<int:pk>', publisher.DetailPublisherView.as_view(), name="publisher"),
    path('add_publisher/', publisher.AddPublisherView.as_view(), name="add_publisher"),
    path('edit_publisher/<int:pk>', publisher.EditPublisherView.as_view(), name="edit_publisher"),
    path('delete_publisher/<int:pk>', publisher.DeletePublisherView.as_view(), name="delete_publisher"),

    # Subject
    path('subjects/', subject.AllSubjectView.as_view(), name="subjects"),
    path('subject/<int:pk>', subject.DetailSubjectView.as_view(), name="subject"),
    path('add_subject/', subject.AddSubjectView.as_view(), name="add_subject"),
    path('edit_subject/<int:pk>', subject.EditSubjectView.as_view(), name="edit_subject"),
    path('delete_subject/<int:pk>', subject.DeleteSubjectView.as_view(), name="delete_subject"),

]







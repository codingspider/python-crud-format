from django.urls import path
from .views import author, publisher, subject, booklanguage, rack, book, studentbookissue, ebook, librarystudent

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

    # Book Language
    path('booklanguages/', booklanguage.AllBookLanguageView.as_view(), name="booklanguages"),
    path('booklanguage/<int:pk>', booklanguage.DetailBookLanguageView.as_view(), name="booklanguage"),
    path('add_booklanguage/', booklanguage.AddBookLanguageView.as_view(), name="add_booklanguage"),
    path('edit_booklanguage/<int:pk>', booklanguage.EditBookLanguageView.as_view(), name="edit_booklanguage"),
    path('delete_booklanguage/<int:pk>', booklanguage.DeleteBookLanguageView.as_view(), name="delete_booklanguage"),

    # Book Rack
    path('racks/', rack.AllRackView.as_view(), name="racks"),
    path('rack/<int:pk>', rack.DetailRackView.as_view(), name="rack"),
    path('add_rack/', rack.AddRackView.as_view(), name="add_rack"),
    path('edit_rack/<int:pk>', rack.EditRackView.as_view(), name="edit_rack"),
    path('delete_rack/<int:pk>', rack.DeleteRackView.as_view(), name="delete_rack"),

    # Book
    path('books/', book.AllBookView.as_view(), name="books"),
    path('book/<int:pk>', book.DetailBookView.as_view(), name="book"),
    path('add_book/', book.AddBookView.as_view(), name="add_book"),
    path('edit_book/<int:pk>', book.EditBookView.as_view(), name="edit_book"),
    path('delete_book/<int:pk>', book.DeleteBookView.as_view(), name="delete_book"),

    # E-Book
    path('ebooks/', ebook.AllEbookView.as_view(), name="ebooks"),
    path('ebook/<int:pk>', ebook.DetailEbookView.as_view(), name="ebook"),
    path('add_ebook/', ebook.AddEbookView.as_view(), name="add_ebook"),
    path('edit_ebook/<int:pk>', ebook.EditEbookView.as_view(), name="edit_ebook"),
    path('delete_ebook/<int:pk>', ebook.DeleteEbookView.as_view(), name="delete_ebook"),

    # Book
    path('bookissues/', studentbookissue.AllBookIssueView.as_view(), name="bookissues"),
    path('bookissue/<int:pk>', studentbookissue.DetailBookIssueView.as_view(), name="bookissue"),
    path('add_bookissue/', studentbookissue.AddBookIssueView.as_view(), name="add_bookissue"),
    path('add_student_bookissue/', studentbookissue.AddBookIssueView.as_view(), name="add_bookissue"),
    path('edit_bookissue/<int:pk>', studentbookissue.EditBookIssueView.as_view(), name="edit_bookissue"),
    path('delete_bookissue/<int:pk>', studentbookissue.DeleteBookIssueView.as_view(), name="delete_bookissue"),


    # Library student member
    # path('librarystudents/', librarystudent.AllLibraryStudentView.as_view(), name="librarystudents"),
    # path('librarystudent/<int:pk>', librarystudent.DetailLibraryStudentView.as_view(), name="librarystudent"),
    # path('add_librarystudent/', librarystudent.AddLibraryStudentView.as_view(), name="add_librarystudent"),
    # path('edit_librarystudent/', librarystudent.AddLibraryStudentView.as_view(), name="edit_librarystudent"),
    # path('delete_librarystudent/<int:pk>', librarystudent.DeleteLibraryStudentView.as_view(), name="delete_librarystudent"),

]

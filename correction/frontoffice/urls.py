from django.urls import path
from .views import complain, phonecalllog, postaldispatch, postalreceive, visitorbook

app_name = 'frontoffice'

urlpatterns = [
    # complain
    path('complains/', complain.AllComplainView.as_view(), name="complains"),
    path('complain/<int:pk>', complain.DetailComplainView.as_view(), name="complain"),
    path('add_complain/', complain.AddComplainView.as_view(), name="add_complain"),
    path('edit_complain/<int:pk>', complain.EditComplainView.as_view(), name="edit_complain"),
    path('delete_complain/<int:pk>', complain.DeleteComplainView.as_view(), name="delete_complain"),

    # complain
    path('phonecalllogs/', phonecalllog.AllPhoneCallLogView.as_view(), name="phonecalllogs"),
    path('phonecalllog/<int:pk>', phonecalllog.DetailPhoneCallLogView.as_view(), name="phonecalllog"),
    path('add_phone_call_log/', phonecalllog.AddPhoneCallLogView.as_view(), name="add_phone_call_log"),
    path('edit_phone_call_log/<int:pk>', phonecalllog.EditPhoneCallLogView.as_view(), name="edit_phone_call_log"),
    path('delete_phone_call_log/<int:pk>', phonecalllog.DeletePhoneCallLogView.as_view(), name="delete_phone_call_log"),

    #postaldispatch
    path('postaldispatchs/', postaldispatch.AllPostalDispatchView.as_view(), name="postaldispatchs"),
    path('postaldispatch/<int:pk>', postaldispatch.DetailPostalDispatchView.as_view(), name="postaldispatch"),
    path('add_postal_dispatch/', postaldispatch.AddPostalDispatchView.as_view(), name="add_postal_dispatch"),
    path('edit_postal_dispatch/<int:pk>', postaldispatch.EditPostalDispatchView.as_view(), name="edit_postal_dispatch"),
    path('delete_postal_dispatch/<int:pk>', postaldispatch.DeletePostalDispatchView.as_view(), name="delete_postal_dispatch"),

    #postalreceive
    path('postalreceives/', postalreceive.AllPostalReceiveView.as_view(), name="postalreceives"),
    path('postalreceive/<int:pk>', postalreceive.DetailPostalReceiveView.as_view(), name="postalreceive"),
    path('add_postal_receive/', postalreceive.AddPostalReceiveView.as_view(), name="add_postal_receive"),
    path('edit_postal_receive/<int:pk>', postalreceive.EditPostalReceiveView.as_view(), name="edit_postal_receive"),
    path('delete_postal_receive/<int:pk>', postalreceive.DeletePostalReceiveView.as_view(), name="delete_postal_receive"),

    # complain
    path('visitorbooks/', visitorbook.AllVisitorBookView.as_view(), name="visitorbooks"),
    path('visitorbook/<int:pk>', visitorbook.DetailVisitorBookView.as_view(), name="visitorbook"),
    path('add_visitor_book/', visitorbook.AddVisitorBookView.as_view(), name="add_visitor_book"),
    path('edit_visitor_book/<int:pk>', visitorbook.EditVisitorBookView.as_view(), name="edit_visitor_book"),
    path('delete_visitor_book/<int:pk>', visitorbook.DeleteVisitorBookView.as_view(),name="delete_visitor_book"),

]







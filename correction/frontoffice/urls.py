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
    path('add_phonecalllog/', phonecalllog.AddPhoneCallLogView.as_view(), name="add_phonecalllog"),
    path('edit_phonecalllog/<int:pk>', phonecalllog.EditPhoneCallLogView.as_view(), name="edit_phonecalllog"),
    path('delete_phonecalllog/<int:pk>', phonecalllog.DeletePhoneCallLogView.as_view(), name="delete_phonecalllog"),

    #postaldispatch
    path('postaldispatchs/', postaldispatch.AllPostalDispatchView.as_view(), name="postaldispatchs"),
    path('postaldispatch/<int:pk>', postaldispatch.DetailPostalDispatchView.as_view(), name="postaldispatch"),
    path('add_postaldispatch/', postaldispatch.AddPostalDispatchView.as_view(), name="add_postaldispatch"),
    path('edit_postaldispatch/<int:pk>', postaldispatch.EditPostalDispatchView.as_view(), name="edit_postaldispatch"),
    path('delete_postaldispatch/<int:pk>', postaldispatch.DeletePostalDispatchView.as_view(), name="delete_postaldispatch"),

    #postalreceive
    path('postalreceives/', postalreceive.AllPostalReceiveView.as_view(), name="postalreceives"),
    path('postalreceive/<int:pk>', postalreceive.DetailPostalReceiveView.as_view(), name="postalreceive"),
    path('add_postalreceive/', postalreceive.AddPostalReceiveView.as_view(), name="add_postalreceive"),
    path('edit_postalreceive/<int:pk>', postalreceive.EditPostalReceiveView.as_view(), name="edit_postalreceive"),
    path('delete_postalreceive/<int:pk>', postalreceive.DeletePostalReceiveView.as_view(), name="delete_postalreceive"),

    # complain
    path('visitorbooks/', visitorbook.AllVisitorBookView.as_view(), name="visitorbooks"),
    path('visitorbook/<int:pk>', visitorbook.DetailVisitorBookView.as_view(), name="visitorbook"),
    path('add_visitorbook/', visitorbook.AddVisitorBookView.as_view(), name="add_visitorbook"),
    path('edit_visitorbook/<int:pk>', visitorbook.EditVisitorBookView.as_view(), name="edit_visitorbook"),
    path('delete_visitorbook/<int:pk>', visitorbook.DeleteVisitorBookView.as_view(),name="delete_visitorbook"),

]







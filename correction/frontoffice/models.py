from django.db import models
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
import os
from .choices import CALL_TYPE, TYPE, choice_status


def validate_image(image):
    file_size = image.file.size
    limit_mb = 2
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_mb)


def validate_file(file):
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf','.doc', '.docx', '.jpg', '.png', '.ppt', '.pptx', '.text']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please choose these  %s file type' % valid_extensions)
    file_size = file.file.size
    limit_mb = 250
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_mb)


class Visitorbook(models.Model):
    purpose = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    meet_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    id_card = models.CharField(max_length=200, null=True)
    date = models.CharField(max_length=255, null=True)
    in_time = models.CharField(max_length=255, null=True)
    out_time = models.CharField(max_length=255, null=True, blank=True)
    note = models.TextField(null=True,blank=True)
    attachment = models.FileField(upload_to='visitorbook', null=True, blank=True, validators=[validate_file])
    date_created = models.DateTimeField(auto_now_add=True)
    active_status = models.IntegerField(null=True, blank=True, default=2)

    def __str__(self):
        return self.name


class Phonecalllog(models.Model):
    name=models.CharField(max_length=200, null=True )
    phone=models.CharField(max_length=200, null=True )
    call_duration=models.CharField(max_length=200, null=True )
    date=models.CharField(max_length=255, null=True)
    followup=models.CharField(max_length=255, null=True, blank=True)
    call_type=models.IntegerField(null=True, choices=CALL_TYPE)
    description=models.TextField(null=True,blank=True)
    note=models.TextField(null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    active_status = models.IntegerField(null=True, blank=True, default=2)

    def __str__(self):
        return self.name


class Postaldispatch(models.Model):
    receiver=models.CharField(max_length=200, null=True )
    sender=models.CharField(max_length=200, null=True )
    referance=models.CharField(max_length=200, null=True )
    dispatch_date=models.CharField(max_length=255, null=True)
    address=models.TextField(null=True)
    note=models.TextField(null=True,blank=True)
    attachment=models.FileField(upload_to='postal', null=True, blank=True,validators=[validate_file])
    date_created=models.DateTimeField(auto_now_add=True)
    active_status = models.IntegerField(null=True, blank=True, default=2)

    def __str__(self):
        return self.receiver


class Postalreceive(models.Model):
    receiver=models.CharField(max_length=200, null=True )
    sender=models.CharField(max_length=200, null=True )
    referance=models.CharField(max_length=200, null=True )
    receive_date=models.CharField(max_length=255, null=True)
    address=models.TextField(null=True)
    note=models.TextField(null=True,blank=True)
    attachment=models.FileField(upload_to='postal', null=True, blank=True,validators=[validate_file])
    date_created=models.DateTimeField(auto_now_add=True)
    active_status = models.IntegerField(null=True, blank=True, default=2)

    def __str__(self):
        return self.receiver


class Complain(models.Model):

    complain_type=models.CharField(max_length=100, null=True, choices=TYPE )
    complain_by=models.ForeignKey(User , null=True  , on_delete=models.SET_NULL)
    phone=models.CharField(max_length=200, null=True )
    date=models.CharField(max_length=255, null=True)
    description=models.TextField(null=True,blank=True)
    action_taken=models.TextField(null=True,blank=True)
    assigned=models.ForeignKey(User , null=True, on_delete=models.SET_NULL, related_name='assigned')
    note=models.TextField(null=True,blank=True)
    attachment=models.FileField(upload_to='postal', null=True, blank=True,validators=[validate_file])
    date_created=models.DateTimeField(auto_now_add=True)
    active_status = models.IntegerField(null=True, blank=True, default=2)

    def __str__(self):
        return self.complain_type

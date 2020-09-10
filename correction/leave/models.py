from django.db import models
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
import os
from .choices import APPLY_STATUS_CHOICE


# -------------------------- leave type-------------------
class LeaveType(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # -------------------------- leave-------------------


def validate_file(file):
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.ppt', '.pptx', '.text']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please choose these  %s file type' % valid_extensions)
    file_size = file.file.size
    limit_mb = 250
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_mb)


class Leave(models.Model):

    applied_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
    leave_type = models.ForeignKey(LeaveType, null=True, on_delete=models.SET_NULL)
    apply_date = models.CharField(max_length=255, null=True)
    from_date = models.CharField(max_length=255, null=True)
    to_date = models.CharField(max_length=255, null=True)
    reason = models.TextField(null=True)
    attachment = models.FileField(upload_to='leave', null=True, blank=True, validators=[validate_file])
    apply_status = models.IntegerField(null=True, choices=APPLY_STATUS_CHOICE)
    approve_status = models.IntegerField(default=0, blank=True)
    active_status = models.IntegerField(null=True, blank=True, default=2)


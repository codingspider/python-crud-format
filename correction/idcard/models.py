from django.db import models

# Create your models here.

SIDE_CHOICES = (
        ('F', 'Front Side'),
        ('B', 'Back Side'),
    )

USER_CHOICES = (
        ('teacher', 'Teacher'),
        ('staff', 'Staff'),
        ('student', 'Student'),
    )


class IdCard(models.Model):
    address = models.TextField()
    background_image = models.ImageField(null=True, blank=True, upload_to='idcard/')
    school_logo = models.ImageField(null=True, blank=True, upload_to='idcard/')
    signature = models.ImageField(null=True, blank=True, upload_to='idcard/')
    school_name = models.CharField(max_length=255, null=True, blank=True)
    id_card_title = models.CharField(max_length=255, null=True, blank=True)
    valid_till = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.id_card_title


class StudentIdCard(models.Model):
    user_id = models.CharField(max_length=255, null=True, blank=True)
    template = models.ForeignKey(IdCard, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=20, choices=USER_CHOICES, null=True)
    id_side = models.CharField(max_length=2, choices=SIDE_CHOICES, null=True)

    def __str__(self):
        return self.name




from django.db import models


class CertificateType(models.Model):
    certificate_name = models.CharField(max_length=255, null=True, blank=True)
    school_name = models.CharField(max_length=255, null=True)
    certificate_text = models.TextField()
    background_image = models.ImageField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    active_status = models.IntegerField(null=True, blank=True, default=2)

    def __str__(self):
        return self.certificate_name


# Generated by Django 3.1.1 on 2020-09-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(blank=True, max_length=255, null=True)),
                ('school_name', models.CharField(max_length=255, null=True)),
                ('certificate_text', models.TextField()),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
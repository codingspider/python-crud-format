# Generated by Django 3.1.1 on 2020-09-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontoffice', '0009_auto_20200909_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitorbook',
            name='image',
        ),
        migrations.AlterField(
            model_name='postalreceive',
            name='receive_date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='visitorbook',
            name='date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='visitorbook',
            name='in_time',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='visitorbook',
            name='out_time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

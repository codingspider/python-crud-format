# Generated by Django 3.1.1 on 2020-09-09 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontoffice', '0010_auto_20200909_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitorbook',
            name='meet_user_type',
        ),
    ]

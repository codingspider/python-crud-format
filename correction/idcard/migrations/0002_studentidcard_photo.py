# Generated by Django 3.1.1 on 2020-09-13 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idcard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentidcard',
            name='photo',
            field=models.ImageField(null=True, upload_to='studentidcard/'),
        ),
    ]

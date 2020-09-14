# Generated by Django 3.1.1 on 2020-09-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idcard', '0002_studentidcard_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentidcard',
            old_name='name',
            new_name='id_card_title',
        ),
        migrations.RenameField(
            model_name='studentidcard',
            old_name='photo',
            new_name='user_photo',
        ),
        migrations.AddField(
            model_name='studentidcard',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='studentidcard',
            name='school_logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='studentidcard',
            name='school_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentidcard',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
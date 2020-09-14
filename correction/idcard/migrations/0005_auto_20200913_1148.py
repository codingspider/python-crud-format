# Generated by Django 3.1.1 on 2020-09-13 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idcard', '0004_auto_20200913_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='idcard/')),
                ('school_logo', models.ImageField(blank=True, null=True, upload_to='idcard/')),
                ('signature', models.ImageField(blank=True, null=True, upload_to='idcard/')),
                ('school_name', models.CharField(blank=True, max_length=255, null=True)),
                ('id_card_title', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='studentidcard',
            old_name='id_card_title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='studentidcard',
            old_name='school_name',
            new_name='student_id',
        ),
        migrations.RemoveField(
            model_name='studentidcard',
            name='address',
        ),
        migrations.RemoveField(
            model_name='studentidcard',
            name='background_image',
        ),
        migrations.RemoveField(
            model_name='studentidcard',
            name='school_logo',
        ),
        migrations.RemoveField(
            model_name='studentidcard',
            name='signature',
        ),
        migrations.AddField(
            model_name='studentidcard',
            name='student_photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
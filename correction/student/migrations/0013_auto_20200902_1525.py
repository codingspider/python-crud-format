# Generated by Django 3.1 on 2020-09-02 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20200902_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_class',
            new_name='class_id',
        ),
    ]
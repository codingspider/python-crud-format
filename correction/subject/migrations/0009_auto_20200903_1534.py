# Generated by Django 3.1 on 2020-09-03 09:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0008_subject_subject_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]

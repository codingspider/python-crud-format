# Generated by Django 3.1 on 2020-09-03 09:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0009_auto_20200903_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='created_at',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]

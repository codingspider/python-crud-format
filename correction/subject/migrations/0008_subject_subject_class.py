# Generated by Django 3.1 on 2020-09-02 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0007_remove_subject_subject_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subject.class'),
        ),
    ]

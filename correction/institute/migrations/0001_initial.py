# Generated by Django 3.1.1 on 2020-09-09 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('bn_name', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('nicename', models.CharField(max_length=255, null=True)),
                ('iso3', models.CharField(max_length=255, null=True)),
                ('numcode', models.IntegerField(null=True)),
                ('phonecode', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('bn_name', models.CharField(max_length=255, null=True)),
                ('lat', models.CharField(max_length=100, null=True)),
                ('lon', models.CharField(max_length=100, null=True)),
                ('url', models.CharField(max_length=100, null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institute.country')),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email_1', models.EmailField(max_length=100)),
                ('email_2', models.EmailField(max_length=100, null=True)),
                ('website', models.URLField(max_length=100)),
                ('institute_code', models.CharField(max_length=100)),
                ('address_1', models.CharField(max_length=500)),
                ('address_2', models.CharField(blank=True, max_length=500, null=True)),
                ('zip', models.CharField(blank=True, max_length=20, null=True)),
                ('latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('established_date', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_1', models.CharField(max_length=15)),
                ('phone_2', models.CharField(blank=True, max_length=15, null=True)),
                ('fax', models.CharField(blank=True, max_length=15, null=True)),
                ('active_status', models.CharField(choices=[('0', 'Select'), ('1', 'Active'), ('2', 'InActive')], default=1, max_length=10)),
                ('agree', models.BooleanField(blank=True, default=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('institute_logo', models.ImageField(blank=True, max_length=255, null=True, upload_to='')),
                ('principle_signature', models.ImageField(blank=True, max_length=255, null=True, upload_to='')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='institute.city')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='institute.country')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='institute.state')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institute.state'),
        ),
    ]

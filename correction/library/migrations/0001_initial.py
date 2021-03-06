# Generated by Django 3.1.1 on 2020-09-10 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('active_status', models.IntegerField(blank=True, default=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('book_number', models.CharField(max_length=200, null=True)),
                ('isbn_number', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('qty', models.IntegerField(null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('status', models.IntegerField(blank=True, default=0, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('active_status', models.IntegerField(blank=True, default=2, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.author')),
            ],
        ),
        migrations.CreateModel(
            name='BookLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('active_status', models.IntegerField(blank=True, default=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('active_status', models.IntegerField(blank=True, default=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField(null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('active_status', models.IntegerField(blank=True, default=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('active_status', models.IntegerField(blank=True, default=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('book_number', models.CharField(max_length=200, null=True)),
                ('isbn_number', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', validators=[library.models.validate_image])),
                ('file', models.FileField(null=True, upload_to='ebook', validators=[library.models.validate_file])),
                ('status', models.IntegerField(blank=True, default=0, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('active_status', models.IntegerField(blank=True, default=2, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.author')),
                ('book_language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.booklanguage')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.publisher')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.subject')),
            ],
        ),
        migrations.CreateModel(
            name='BookIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, default=0, null=True)),
                ('issue_date', models.DateTimeField(null=True)),
                ('return_date', models.DateTimeField(null=True)),
                ('active_status', models.IntegerField(blank=True, default=2, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.book')),
                ('issued_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issued_by', to=settings.AUTH_USER_MODEL)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.booklanguage'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='rack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.rack'),
        ),
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.subject'),
        ),
    ]

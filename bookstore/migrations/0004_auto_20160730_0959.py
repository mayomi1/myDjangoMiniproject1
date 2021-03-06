# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-30 09:59
from __future__ import unicode_literals

import bookstore.validate
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_auto_20160730_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='book_cover',
            field=models.FileField(upload_to=b'', validators=[bookstore.validate.validate_file_extension_image]),
        ),
        migrations.AlterField(
            model_name='addbook',
            name='category',
            field=models.CharField(choices=[('SOFTWARE', 'Software_books'), ('HARDWARE', 'Hardware_books'), ('NETWORKING', 'Networking_books'), ('PROGRAMMING', 'programming_books'), ('LECTURE_NOTES', 'lecture_notes'), ('OTHERS', 'others')], max_length=50),
        ),
    ]

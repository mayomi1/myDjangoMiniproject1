# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 14:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_auto_20160801_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addbook',
            old_name='image',
            new_name='book_cover',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0002_image_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
    ]
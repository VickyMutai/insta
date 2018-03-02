# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gram', '0002_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('caption', models.CharField(max_length=60)),
                ('comments', models.CharField(max_length=60)),
                ('likes', models.CharField(max_length=30)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['upload_date'],
            },
        ),
    ]
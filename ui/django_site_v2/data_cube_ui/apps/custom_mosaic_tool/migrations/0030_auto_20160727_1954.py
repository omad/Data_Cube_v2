# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_mosaic_tool', '0029_metadata_percentage_clean_pixels'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='description',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='query',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]

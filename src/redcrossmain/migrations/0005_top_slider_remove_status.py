# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redcrossmain', '0004_alert_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='top_slider',
            name='remove_status',
            field=models.BooleanField(default=False),
        ),
    ]

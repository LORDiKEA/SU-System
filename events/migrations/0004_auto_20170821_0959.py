# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170821_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]

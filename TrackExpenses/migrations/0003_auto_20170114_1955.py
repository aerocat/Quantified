# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrackExpenses', '0002_auto_20170114_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='added_on_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 20:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrackExpenses', '0003_auto_20170114_1955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]

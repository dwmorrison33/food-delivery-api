# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-27 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0002_auto_20170527_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, default='', upload_to='restaurant_logo/'),
        ),
    ]

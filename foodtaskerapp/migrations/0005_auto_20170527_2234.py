# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-27 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0004_auto_20170527_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.FileField(blank=True, default='', upload_to='restaurant_logo/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20170214_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nrstc',
            name='place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

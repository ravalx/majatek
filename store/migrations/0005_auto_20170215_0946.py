# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20170214_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nrst',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='nrstc',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]

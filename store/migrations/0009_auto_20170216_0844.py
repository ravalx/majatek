# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 08:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20170216_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nrst',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.RegexValidator('^\\d*\\.\\d{2}$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]

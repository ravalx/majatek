# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20170209_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nrstc',
            name='data_przyjecia',
            field=models.DateField(null=True),
        ),
    ]
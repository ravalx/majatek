# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20170209_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nrstc',
            name='data',
            field=models.DateField(null=True),
        ),
    ]
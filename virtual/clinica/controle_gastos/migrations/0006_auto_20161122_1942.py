# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 22:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_gastos', '0005_auto_20161112_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='data',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
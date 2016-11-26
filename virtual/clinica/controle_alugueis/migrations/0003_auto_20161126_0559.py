# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 08:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_alugueis', '0002_auto_20161126_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='nome_invalido', message='Nome invalido', regex='^[a-zA-Z *]+$')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(code='telefone_invalido', message='Numero de telefone invalido', regex='^(\\d\\d)\\d{5}-\\d{4}$')]),
        ),
    ]

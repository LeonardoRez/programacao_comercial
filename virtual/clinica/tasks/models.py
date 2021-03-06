# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .const import GRAU_IMPORTANCIA

# Create your models here.
class Tarefa(models.Model):
    texto = models.CharField(max_length=40)
    done = models.BooleanField(default = False)
    grau_importancia = models.IntegerField(choices=GRAU_IMPORTANCIA, default = 3)

    def __str__(self):
        return self.texto

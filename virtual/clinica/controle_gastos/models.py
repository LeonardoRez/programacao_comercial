# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from const import *

# Create your models here.
class Gasto(models.Model):
    tipo_gasto = models.IntegerField(choices=TIPO_GASTO, default=11)
    custo = models.DecimalField(max_digits = 6, decimal_places=2)
    descricao = models.CharField(max_length = 200)
    data = models.DateTimeField(default = datetime.now, blank = True)

    def __str__(self):
        return '{0} - {1}'.format(self.get_tipo_gasto_display(), self.descricao)

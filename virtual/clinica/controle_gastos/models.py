from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    nome_gasto = models.CharField(max_length = 100)
    custo = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.CharField(max_length = 1000)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_gasto

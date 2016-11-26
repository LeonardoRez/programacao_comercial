# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import *
from django.utils import timezone

from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length = 50,
                            validators = [
                                    RegexValidator(regex=r'^[a-zA-Z *]+$', message=("Nome invalido"), code='nome_invalido')
                                    ]
                            )
    telefone = models.CharField(
                            max_length = 14,
                            validators = [
                                    RegexValidator(regex=r'^\(\d\d\)\d{5}-\d{4}$',
                                        message = ("Numero de telefone invalido"),
                                        code = 'telefone_invalido')
                                    ]
                            )
    observacao = models.CharField(max_length = 200, blank = True)

    def __str__(self):
        return self.nome


class Aluguel(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateField(auto_now = False)
    horaInicio = models.TimeField()
    horaTermino = models.TimeField()

    def __str__(self):
        return '{0}, dia: {1}, {2}-{3}'.format(self.cliente, self.data, self.horaInicio, self.horaTermino)

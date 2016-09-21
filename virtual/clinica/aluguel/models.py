from __future__ import unicode_literals

from django.db import models


class Sala(models.Model):
    num_sala  = models.IntegerField()
    categoria = models.IntegerField()


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    sala = models.ForeignKey(Sala, on_delete = models.CASCADE)
    rg = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    endereco = Endereco()
    telefone  = models.CharField(max_length=12)
    data_cadastro = models.CharField(max_length=10)
    profissao = models.CharField(max_length=100)
    finalidadeSala = models.CharField(max_length=300)
    #historico_reserva = HistoricoReserva()

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_reserva = models.CharField(max_length=10)
    periodoHora = models.CharField(max_length=50)
    #preco
    data_pagamento = models.CharField(max_length=10)

class Endereco(models.Model):
    bairro = models.CharField(max_lenght=30)
    rua = models.CharField(max_lenght=30)
    numero = models.CharField(max_lenght=5)
    cidade = models.CharField(max_lenght=30)

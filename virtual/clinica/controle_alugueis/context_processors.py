# -*- coding: utf-8 -*-
from .models import Aluguel, Cliente
from django.db.models import Sum
from datetime import datetime

def total_arrecadado(request):
    # ARRECADADO COM ALUGUEL
    contexto = {}
    quant = Aluguel.objects.filter(data__month = datetime.now().month).aggregate(Sum('valor')).get('valor__sum')
    if quant is None or quant == 0:
        contexto['arrecadado_mes'] = 0
    else:
        contexto['arrecadado_mes'] = quant
    # QUANTIDADE DE CLIENTES CADASTRADOS
    quant_cliente = len(Cliente.objects.all())
    if quant_cliente is None or quant_cliente == 0:
        contexto['quant_clientes'] = 0
    else:
        contexto['quant_clientes'] = quant_cliente


    return contexto

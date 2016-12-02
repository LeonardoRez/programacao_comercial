# -*- coding: utf-8 -*-
from .models import Gasto
from django.db.models import Sum
from datetime import datetime

def total_gasto(request):
    #ultimas_tarefas = Tarefa.objects.filter().order_by('grau_importancia', 'id')[:5]
    contexto = {}
    quant = Gasto.objects.filter(data__month = datetime.now().month).aggregate(Sum('custo')).get('custo__sum')
    if quant is None or quant == 0:
        contexto['gasto_mes'] = 0
    else:
        contexto['gasto_mes'] = quant
    return contexto

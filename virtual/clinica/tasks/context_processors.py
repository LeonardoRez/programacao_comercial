# -*- coding: utf-8 -*-
from .models import Tarefa


def ultimas_tasks(request):
    contexto = {}
    contexto['ultimas_tarefas'] = Tarefa.objects.filter(done = False).order_by('grau_importancia','id')[:5]
    contexto['quant_total'] = len(Tarefa.objects.filter(done = False))
    contexto['quant_urgente'] = len(Tarefa.objects.filter(grau_importancia = 1,done = False))
    contexto['quant_importante'] = len(Tarefa.objects.filter(grau_importancia = 2,done = False))
    contexto['quant_simples'] = len(Tarefa.objects.filter(grau_importancia = 3,done = False))
    contexto['quant_lembrete'] = len(Tarefa.objects.filter(grau_importancia = 4,done = False))

    return contexto

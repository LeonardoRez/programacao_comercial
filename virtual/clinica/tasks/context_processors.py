# -*- coding: utf-8 -*-
from .models import Tarefa


def ultimas_tasks(request):
    #ultimas_tarefas = Tarefa.objects.filter().order_by('grau_importancia', 'id')[:5]
    ultimas_tarefas = Tarefa.objects.filter().order_by('grau_importancia','id')[:5]
    return {'ultimas_tarefas' : ultimas_tarefas}

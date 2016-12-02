# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from datetime import datetime
from const import *
from .models import *
from .forms import *

class ListarTarefas(LoginRequiredMixin, ListView):
    login_url='/'
    model = Tarefa
    form_class = FormularioTarefa
    template_name = 'tasks/listar_tarefas.html'

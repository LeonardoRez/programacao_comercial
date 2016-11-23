# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from datetime import datetime
from .models import Gasto
from .forms import FormularioGasto
from django.utils import timezone
from const import *

# Create your views here.
class Gastos(LoginRequiredMixin, ListView):
    login_url='/'
    model = Gasto
    form_class = FormularioGasto
    template_name = 'controle_gastos/listar.html'

    def get_context_data(self, **kwargs):


        self.context = super(Gastos, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Lista de Gastos'
        self.context['custo_total'] = self.get_queryset().aggregate(Sum('custo')).get('custo__sum')
        self.context['meses'] = MESES

        self.context['mes']  = int(self.request.GET.get("mes", 0))
        self.context['form'] = FormularioGasto()
        return self.context

    def get_queryset(self):
        mes = self.request.GET.get("mes") # LISTAR GASTOS POR MES. FALTA CRIAR UM SELECT PARA MANDAR O VALOR PARA ESSE 'mes'
        if mes is None:
            queryset = Gasto.objects.filter()
        else:
            queryset = Gasto.objects.filter(data__month = mes)
        return queryset


class NovoGasto(LoginRequiredMixin, CreateView):
    """
    View para a criação de novos gastos.
    """
    model = Gasto
    form_class = FormularioGasto
    template_name = 'controle_gastos/novo.html'
    success_url = reverse_lazy('listar-gastos')

    def get_context_data(self, **kwargs):
        self.context = super(NovoGasto, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Adicionar Gasto'
        return self.context

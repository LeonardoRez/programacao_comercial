# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Gasto
from .forms import FormularioGasto
from django.utils import timezone

# Create your views here.
class Gastos(LoginRequiredMixin, ListView):
    login_url='/'
    model = Gasto
    form_class = FormularioGasto
    template_name = 'controle_gastos/listar.html'
    context = {}

    def get_context_data(self, **kwargs):
        temp = self.context['custo_total']
        self.context = super(Gastos, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Lista de Gastos'
        self.context['custo_total'] = temp
        self.context['test'] = FormularioGasto()
        return self.context

    def get_queryset(self):
        mes = 11 # LISTAR GASTOS POR MES. FALTA CRIAR UM SELECT PARA MANDAR O VALOR PARA ESSE 'mes'
        if mes == '':
            queryset = Gasto.objects.filter()
        else:
            queryset = Gasto.objects.filter(data__month = mes)
        # qt = Gasto.objects.aggregate(Sum('custo'))
        qt = 0
        for i in range(0,len(queryset)):
            qt += queryset[i].custo
        self.context['custo_total'] = qt
        return queryset

    def teste(self):
        print type(Gasto.objects.filter())


class NovoGasto(LoginRequiredMixin, CreateView):
    """
    View para a criação de novos gastos.
    """
    model = Gasto
    form_class = FormularioGasto
    template_name = 'controle_gastos/novo.html'
    success_url = reverse_lazy('listar-gastos')

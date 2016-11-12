# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Gasto
from .forms import FormularioGasto
from django.utils import timezone

# Create your views here.
class Gastos(LoginRequiredMixin, ListView):
    model = Gasto
    template_name = 'controle_gastos/listar.html'

    def get_context_data(self, **kwargs):
        context = super(Gastos, self).get_context_data(**kwargs)
        context['teste'] = timezone.now()
        context['teste2'] = '\tteste'
        return context

    def get_queryset(self):
        queryset = Gasto.objects.filter()
        return queryset


class NovoGasto(LoginRequiredMixin, CreateView):
    """
    View para a criação de novos gastos.
    """
    model = Gasto
    form_class = FormularioGasto
    template_name = 'controle_gastos/novo.html'
    success_url = reverse_lazy('listar-gastos')

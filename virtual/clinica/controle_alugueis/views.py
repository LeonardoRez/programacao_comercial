# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import FormularioCliente









class NovoCliente(LoginRequiredMixin, CreateView):
    """
    View para criação de novos clientes
    """
    model = Cliente
    form_class = FormularioCliente
    template_name = 'controle_alugueis/novo_cliente.html'
    success_url = reverse_lazy('cadastrar-clientes')

    def get_context_data(self, **kwargs):
        self.context = super(NovoCliente, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Novo Cliente'
        return self.context

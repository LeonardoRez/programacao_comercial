# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *









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


class NovoAluguel(LoginRequiredMixin, CreateView):
    """
    View para criação de novos alugueis
    """
    model = Aluguel
    form_class = FormularioAluguel
    template_name = 'controle_alugueis/novo_aluguel.html'
    success_url = reverse_lazy('cadastrar-alugueis')

    def get_context_data(self, **kwargs):
        self.context = super(NovoAluguel, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Novo aluguel'
        return self.context

    """
    def clean(self):
        super(NovoAluguel, self).clean()
        hInicio = self.cleaned_data.get("horaInicio")
        hTermino = self.cleaned_data.get("horaTermino")
        if hInicio > hTermino:
            self.add_error('horaInicio',"Hora de término não pode ser maior que de inicio")
    """

class UpdateAluguel(LoginRequiredMixin, UpdateView):
    model = Aluguel
    #fields = ['cliente']
    form_class = FormUpdateAluguel
    template_name = 'controle_alugueis/update_aluguel.html'
    success_url = reverse_lazy('cadastrar-alugueis')
    def get_context_data(self, **kwargs):
        self.context = super(UpdateAluguel, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Update aluguel'
        return self.context

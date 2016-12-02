# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *




class NovoCliente(LoginRequiredMixin, CreateView):
    """
    View para criação de novos clientes
    """
    login_url='/'
    model = Cliente
    form_class = FormularioCliente
    template_name = 'controle_alugueis/novo_cliente.html'
    success_url = reverse_lazy('listar-clientes')

    def get_context_data(self, **kwargs):
        self.context = super(NovoCliente, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Novo Cliente'
        return self.context
class ListarClientes(LoginRequiredMixin, ListView):
    """
    View para listar os clientes cadastrados
    """
    login_url = '/'
    model = Cliente
    template_name = 'controle_alugueis/listar_clientes.html'

    def get_context_data(self, **kwargs):
        self.context = super(ListarClientes, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Clientes'
        self.context['form'] = FormularioCliente()
        return self.context

    def get_queryset(self):
        queryset = Cliente.objects.filter()
        return queryset
class UpdateCliente(LoginRequiredMixin, UpdateView):
    """
    View para atualizar dados de um cliente
    """
    login_url='/'
    model = Cliente
    form_class = FormUpdateCliente
    template_name = 'controle_alugueis/update_cliente.html'
    success_url = reverse_lazy('listar-clientes')
    def get_context_data(self, **kwargs):
        self.context = super(UpdateCliente, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Atualizar cliente'
        return self.context

class DeletarCliente(LoginRequiredMixin, DeleteView):
    login_url = '/'
    model = Cliente
    form_class = FormularioCliente
    success_url = reverse_lazy('listar-clientes')
    template_name = 'controle_alugueis/deletar_cliente.html'
    def get_context_data(self, **kwargs):
        self.context = super(DeletarCliente, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Deletar cliente'
        return self.context

class NovoAluguel(LoginRequiredMixin, CreateView):
    """
    View para criação de novos alugueis
    """
    login_url='/'
    model = Aluguel
    form_class = FormularioAluguel
    template_name = 'controle_alugueis/novo_aluguel.html'
    success_url = reverse_lazy('listar-alugueis')

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
    login_url='/'
    model = Aluguel
    form_class = FormUpdateAluguel
    template_name = 'controle_alugueis/update_aluguel.html'
    success_url = reverse_lazy('cadastrar-alugueis')
    def get_context_data(self, **kwargs):
        self.context = super(UpdateAluguel, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Update aluguel'
        return self.context

class ListarAlugueis(LoginRequiredMixin, ListView):
    login_url='/'
    model = Aluguel
    template_name = 'controle_alugueis/listar_alugueis.html'

    def get_context_data(self, **kwargs):
        self.context = super(ListarAlugueis, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Alugueis'
        self.context['form'] = FormularioAluguel()
        return self.context

    def get_queryset(self):
        queryset = Aluguel.objects.filter()
        return queryset

# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from veiculos.models import *
from veiculos.forms import *

class VeiculosList(ListView):
    model = Veiculo
    template_name = 'veiculos/listar.html'

class VeiculosNew(CreateView):
    """
    View para a criação de novos veiculos.
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculos/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class VeiculosEdit(UpdateView):
    """
    View para a edição de veiculos já cadastrados.
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculos/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class VeiculosDelete(DeleteView):
    """
    View para a exclusão de veiculos.
    """
    model = Veiculo
    template_name = 'veiculos/deletar.html'
    success_url = reverse_lazy('listar-veiculos')

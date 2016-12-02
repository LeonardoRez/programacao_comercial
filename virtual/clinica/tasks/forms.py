# -*- coding: utf-8 -*-
from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from functools import partial


class FormularioTarefa(forms.ModelForm):
    """
    Formulario para o model Gasto
    """
    class Meta:
        model = Tarefa
        exclude = []
    # widgets = {
    #     'tipo_gasto': forms.Select(attrs={'class': 'form-control'}),
    #     'custo': forms.NumberInput(attrs={'class': 'form-control has-feedback-left'}),
    #     'descricao': forms.TextInput(attrs={'class': 'form-control has-feedback-left'}),
    #     'data': forms.DateTimeInput(attrs={'class': 'form-control has-feedback-left'}),
    # }
# MUDAR CSS
    def __init__(self, *args, **kwargs):
        super(FormularioTarefa, self).__init__(*args, **kwargs)

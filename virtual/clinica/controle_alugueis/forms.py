# -*- coding: utf-8 -*-
from django import forms
from .models import *


class FormularioCliente(forms.ModelForm):
    """
    Formulario para o model Cliente
    """
    class Meta:
        model = Cliente
        exclude = []

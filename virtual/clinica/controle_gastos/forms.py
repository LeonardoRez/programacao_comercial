# -*- coding: utf-8 -*-
from django import forms
from controle_gastos.models import *
class FormularioGasto(forms.ModelForm):
 """
 Formulario para o model Gasto
 """
 class Meta:
     model = Gasto
     exclude = []

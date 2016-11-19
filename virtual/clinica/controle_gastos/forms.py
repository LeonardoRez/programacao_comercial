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
# MUDAR CSS
    #  def __init__(self, *args, **kwargs):
    #      super(FormularioPedido, self).__init__(*args, **kwargs)
    #      self.fields['custo'].widget.attrs['class'] = 'form-control has-feedback-left'

# -*- coding: utf-8 -*-
from django import forms
from controle_gastos.models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class FormularioGasto(forms.ModelForm):
    """
    Formulario para o model Gasto
    """
    class Meta:
        model = Gasto
        exclude = []
# MUDAR CSS
    def __init__(self, *args, **kwargs):
        super(FormularioGasto, self).__init__(*args, **kwargs)
        self.fields['tipo_gasto'].widget.attrs['class'] = 'form-control pull-right'
        self.fields['descricao'].widget.attrs['class'] = 'form-control has-feedback-left'
        self.fields['custo'].widget.attrs['class'] = 'form-control has-feedback-left'
        self.fields['data'].widget.attrs['class'] = 'form-control has-feedback-left'
        self.fields['data'].widget.attrs['id'] = 'datepicker'

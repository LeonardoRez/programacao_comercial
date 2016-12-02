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
# MUDAR CSS
    def __init__(self, *args, **kwargs):
        super(FormularioTarefa, self).__init__(*args, **kwargs)
        self.fields['texto'].widget.attrs['class'] = 'form-control'
        self.fields['done'].widget.attrs['class'] = 'has-feedback-left checkbox'
        self.fields['grau_importancia'].widget.attrs['class'] = 'form-control has-feedback-left'

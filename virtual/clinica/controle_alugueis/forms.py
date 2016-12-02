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
    def __init__(self, *args, **kwargs):
        super(FormularioCliente, self).__init__(*args, **kwargs)
        #NOME
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['pattern'] = '[a-zA-Z *]+'
        self.fields['nome'].widget.attrs['title'] = 'Somente letras'
        #TELEFONE
        self.fields['telefone'].widget.attrs['class'] = 'form-control'
        self.fields['telefone'].widget.attrs['data-inputmask'] = '\"mask\": \"(99)99999-9999\"'
        self.fields['telefone'].widget.attrs['data-mask'] = ""
        #OBSERVACAO
        self.fields['observacao'].widget.attrs['class'] = 'form-control'

class FormularioAluguel(forms.ModelForm):
    """
    Formulario para o model Aluguel
    """
    class Meta:
        model = Aluguel
        exclude = []
    def __init__(self,*args,**kwargs):
        super(FormularioAluguel, self).__init__(*args,**kwargs)

class FormUpdateAluguel(forms.ModelForm):
    class Meta:
        model = Aluguel
        exclude = []

class FormUpdateCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = []
    def __init__(self, *args, **kwargs):
        super(FormUpdateCliente, self).__init__(*args, **kwargs)
        #NOME
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['pattern'] = '[a-zA-Z *]+'
        self.fields['nome'].widget.attrs['title'] = 'Somente letras'
        #TELEFONE
        self.fields['telefone'].widget.attrs['class'] = 'form-control'
        self.fields['telefone'].widget.attrs['data-inputmask'] = '\"mask\": \"(99)99999-9999\"'
        self.fields['telefone'].widget.attrs['data-mask'] = ""
        #OBSERVACAO
        self.fields['observacao'].widget.attrs['class'] = 'form-control'

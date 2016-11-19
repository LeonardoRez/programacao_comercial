# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Autenticacao(View):
    def get(self,request):
        if request.user.is_authenticated():
            return redirect(reverse('index'))
        else:
            return render(request,'autenticacao/login.html', {})

    def post(self,request):
        resposta={
            'sucesso': False,
            'mensagem': '',
            'login':'',
        }
        usuario = request.POST.get("login")
        senha = request.POST.get("senha")
        user = authenticate(username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect('/index')
        else:
            resposta['mensagem'] = 'Login ou Senha incorreto(s)'
            resposta['login'] = usuario

        return render(request, 'autenticacao/login.html', resposta)

class Logout(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        return redirect('login')


# def login(request):
#     # return HttpRespéonse("Tela de login")
#     # template = loader.get_template('autenticacao/index.html')
#     return render(request, 'autenticacao/login.html', {})
class Index(LoginRequiredMixin,View):
    login_url='/'
    def get(self,request):
        dados={
            'titulo':'Inicio'
        }
        return render(request,'index.html',dados)
    def logout(self,request):
        auth_logout(request)

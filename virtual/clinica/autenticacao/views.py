from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Autenticacao(View):
    def get(self,request):
        return render(request,'autenticacao/login.html', {})

    def post(self,request):
        resposta={
            'sucesso': False,
            'mensagem': ''
        }
        usuario = request.POST.get("login")
        senha = request.POST.get("senha")
        user = authenticate(username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect('/index')
        else:
            resposta['mensagem'] = 'Login ou Senha incorreto(s)'

        return render(request, 'autenticacao/login.html', resposta)

# def login(request):
#     # return HttpResponse("Tela de login")
#     # template = loader.get_template('autenticacao/index.html')
#     return render(request, 'autenticacao/login.html', {})

def index(request):
    return render(request,'index.html',{})

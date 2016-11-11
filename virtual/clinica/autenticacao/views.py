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
            'mensagem': '',
            'login':'',
        }
        usuario = request.POST.get("login")
        senha = request.POST.get("senha")
        user = authenticate(username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect('/', )
        else:
            resposta['mensagem'] = 'Login ou Senha incorreto(s)'
            resposta['login'] = usuario

        return render(request, 'autenticacao/login.html', resposta)

# def login(request):
#     # return HttpResponse("Tela de login")
#     # template = loader.get_template('autenticacao/index.html')
#     return render(request, 'autenticacao/login.html', {})
class Index(LoginRequiredMixin,View):
    login_url='/login'
    def get(self,request):
        dados={
            'nome':'',
            'data_cadastro':'',
            'titulo':'Inicio'
        }
        if request.user.is_authenticated():
            dados['nome'] = request.user.first_name
            dados['data_cadastro'] = request.user.date_joined.year
        return render(request,'index.html',dados)

def index(request):
    return render(request,'index.html',{})

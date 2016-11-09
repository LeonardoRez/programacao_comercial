from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def login(request):
    # return HttpResponse("Tela de login")
    # template = loader.get_template('autenticacao/index.html')
    return render(request, 'autenticacao/login.html', {})

def index(request):
    return render(request,'index.html',{})

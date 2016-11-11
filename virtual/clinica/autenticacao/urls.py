from django.conf.urls import url
from . import views #views no mesmo diretorio

urlpatterns = [
    url(r'^login', views.Autenticacao.as_view(), name='login'), # chama a tela de login quando a url eh /login
    url(r'^$', views.Index.as_view(), name='index'), # chama a classe Index quando a url eh /

]

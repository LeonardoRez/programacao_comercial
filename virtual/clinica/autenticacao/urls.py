from django.conf.urls import url
from . import views #views no mesmo diretorio

urlpatterns = [
    url(r'^login', views.login, name='login'), # chama a tela de login quando a url eh /login
    url(r'^$', views.index, name='index'), # chama o index quando a url eh /

]

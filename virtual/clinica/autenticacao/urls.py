from django.conf.urls import url
from . import views #views no mesmo diretorio

urlpatterns = [
    url(r'^$', views.login, name='login'), # chama index quando a url e gastos/
]

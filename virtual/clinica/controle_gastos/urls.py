from django.conf.urls import url
from . import views #views no mesmo diretorio

urlpatterns = [
    url(r'^$', views.index, name='gastos'), # chama index quando a url e gastos/
]

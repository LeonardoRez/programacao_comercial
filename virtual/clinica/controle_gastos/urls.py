from django.conf.urls import url
from . import views #views no mesmo diretorio

urlpatterns = [
    url(r'^gastos/', views.index, name='test'), # chama index quando a url e gastos/
]

from django.conf.urls import url
from . import views #views no mesmo diretorio

urlpatterns = [
    url(r'^$', views.ListarTarefas.as_view(), name='listar-tarefas'), # chama index quando a url e gastos/
    url(r'^nova/$', views.NovaTarefa.as_view(), name='nova-tarefa'),
]

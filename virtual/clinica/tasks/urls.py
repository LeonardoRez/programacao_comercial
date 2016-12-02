from django.conf.urls import url
from . import views #views no mesmo diretorio

urlpatterns = [
    url(r'^$', views.ListarTarefas.as_view(), name='listar-tarefas'), # chama index quando a url e gastos/
    url(r'^nova/$', views.NovaTarefa.as_view(), name='nova-tarefa'),
    url(r'^update/(?P<pk>[\w-]+)$',views.UpdateTarefa.as_view(), name = 'atualizar-tarefa'),
    url(r'^deletar/(?P<pk>[\w-]+)$',views.DeletarTarefa.as_view(), name = 'deletar-tarefa'),
]

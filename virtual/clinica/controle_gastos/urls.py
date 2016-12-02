from django.conf.urls import url
from . import views #views no mesmo diretorio

urlpatterns = [
    url(r'^$', views.Gastos.as_view(), name='listar-gastos'), # chama index quando a url e gastos/
    url(r'^novo/$', views.NovoGasto.as_view(), name='novo-gasto'),
    url(r'^update/(?P<pk>[\w-]+)$',views.UpdateGasto.as_view(), name = 'atualizar-gasto'),
    url(r'^deletar/(?P<pk>[\w-]+)$',views.DeletarGasto.as_view(), name = 'deletar-gasto'),
]

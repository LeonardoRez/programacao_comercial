from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^clientes/$',views.ListarClientes.as_view(), name = 'listar-clientes'),
    url(r'^clientes/novo/$',views.NovoCliente.as_view(), name = 'cadastrar-clientes'),
    url(r'^clientes/update/(?P<pk>[\w-]+)$',views.UpdateCliente.as_view(), name = 'atualizar-clientes'),
    url(r'^clientes/deletar/(?P<pk>[\w-]+)$',views.DeletarCliente.as_view(), name = 'deletar-clientes'),
    # url(r'^listar/',views.Aluguel.as_view(), name = 'listar-alugueis'),
    url(r'^$',views.ListarAlugueis.as_view(), name = 'listar-alugueis'),
    url(r'^novo/$',views.NovoAluguel.as_view(), name = 'cadastrar-alugueis'),
    url(r'^update/(?P<pk>[\w-]+)$',views.UpdateAluguel.as_view(), name = 'atualizar-alugueis'),

]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^clientes/novo/$',views.NovoCliente.as_view(), name = 'cadastrar-clientes'),
    # url(r'^listar/',views.Aluguel.as_view(), name = 'listar-alugueis'),
    url(r'^novo/$',views.NovoAluguel.as_view(), name = 'cadastrar-alugueis'),

]

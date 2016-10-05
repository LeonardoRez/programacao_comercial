from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mes_id>[1-12]+)/$', views.agendaMes, name='agendaMes'),
    url(r'^(?P<semana_id>[0-5]+)/(?P<mes_id>[1-12]+)/$', views.agendaSemana, name='agendaSemna'),
]

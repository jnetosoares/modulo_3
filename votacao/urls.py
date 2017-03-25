from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /votacao/
    url(r'^$', views.index, name='index'),
    # ex: /votacao/5/
    url(r'^(?P<pergunta_id>[0-9]+)/$', views.detalhes, name='detalhes'),
    # ex: /votacao/5/resultado/
    url(r'^(?P<pergunta_id>[0-9]+)/resultado/$', views.resultado, name='resultado'),
    # ex: /votacao/5/voto/
    url(r'^(?P<pergunta_id>[0-9]+)/voto/$', views.voto, name='voto'),
]
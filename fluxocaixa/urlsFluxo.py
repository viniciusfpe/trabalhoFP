from django.conf.urls import patterns, include, url

urlpatterns = patterns('fluxocaixa.views',
    url(r'^$', 'fluxoListar'),
    url(r'^pesquisar/$', 'fluxoPesquisar'),
    url(r'^imprimir/$', 'fluxoImprimir'),
)
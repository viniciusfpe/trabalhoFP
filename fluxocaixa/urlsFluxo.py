from django.conf.urls import patterns, include, url

urlpatterns = patterns('fluxocaixa.views',
    url(r'^$', 'fluxoListar'),
)
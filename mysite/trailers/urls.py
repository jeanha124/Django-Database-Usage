from django.conf.urls import patterns, url
from trailers import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<trailer_index>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<trailer_index>\d+)/results/S', views.results, name='results'),
    url(r'^(?P<trailer_index>\d+)/vote/$', views.vote, name='vote'),

)

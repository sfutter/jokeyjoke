from django.conf.urls import patterns, url

from jokes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<joke_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<joke_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<joke_id>\d+)/like/$', views.like, name='like'),
)
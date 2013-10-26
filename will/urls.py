from django.conf.urls import patterns, url

from will import views



urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<testator_id>\d+)/$', views.detail, name = 'detail'),
    url(r'^newperson/(?P<action>\w+)/(?P<testator_id>\d+)/$', views.newperson, name = 'newperson'),
    url(r'^(?P<testator_id>\d+)/results/$', views.results, name="results"),
    url(r'^(?P<testator_id>\d+)/(?P<action>\w+)/(?P<relID>\d+)/$', views.edit, name="edit"),
    url(r'^input/$', views.input, name='input'),
)

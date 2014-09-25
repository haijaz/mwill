from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mwill.views.home', name='home'),
    # url(r'^mwill/', include('mwill.foo.urls')),
    url(r'^register/(?P<action>\w+)', views.register, name="register"),
    url(r'^register/', views.register, name="register"),
    url(r'^$', views.index, name="index"),
    url(r'^will/', include('will.urls', namespace = "will")),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
)

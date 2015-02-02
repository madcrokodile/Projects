from django.conf.urls import patterns, url

from nagios_alerts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
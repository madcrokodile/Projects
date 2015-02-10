from django.conf.urls import patterns, include, url
from django.contrib import admin




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^dashboard/', include('nagios_alerts.urls')),
    url(r'^dash/', include('nagios_alerts.urls')),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^testing/', include('nagios_alerts.urls')),
)

from django.http import HttpResponse
import datetime
from django.template import RequestContext, loader, Template
from django.shortcuts import  render
from nagios_alerts.models import Servers




def index(request):
    server_name = Servers.objects
#    server_name = Servers.objects

    # это пока критикал, красный
    #    server_status = 'F51414'
    # а это клёвый желтый ворнинг
    server_status = 'F5EC14'
    service_name = ['http', 'ftp', 'ssh', 'nginx']
    service_duration = '12.13'
    service_status_message = 'всё пропало, всё пропалооо!!!'

    dash_template = loader.get_template('nagios_alerts/index.html')

    context = RequestContext(request,
        {'server_name' : server_name,
         'server_status' : server_status,
         'service_name' : service_name,
         'service_duration' : service_duration,
         'service_status_message' : service_status_message
        }
    )
    html = dash_template.render(context)
    return HttpResponse(html)

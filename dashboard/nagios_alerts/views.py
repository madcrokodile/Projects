from array import array
from django.http import HttpResponse
import datetime
from django.template import RequestContext, loader, Template
from django.shortcuts import  render


def index(request):
    server_list = [1, 2, 3]
    dash_template = loader.get_template('nagios_alerts/index2.html')
    context = RequestContext(request,
        {'server_list' : server_list}
    )
    html = dash_template.render(context)
    return HttpResponse(html)

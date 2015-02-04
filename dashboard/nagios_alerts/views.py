from django.http import HttpResponse
import datetime
from django.template import RequestContext, loader, Template
from django.shortcuts import  render


def index(request):
    dash_template = loader.get_template('nagios_alerts/index.html')
    context = RequestContext(request,{})
    html = dash_template.render(context)
    return HttpResponse(html)

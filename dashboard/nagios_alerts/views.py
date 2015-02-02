from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('nagios_alerts/index.html')
    return HttpResponse(template)




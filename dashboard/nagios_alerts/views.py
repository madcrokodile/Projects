from django.http import HttpResponse
from django.template import RequestContext, loader, Template
from django.shortcuts import  render


#def index(request):
#    template = loader.get_template('nagios_alerts/index2.html')
#    return HttpResponse()
#    return render_to_response(template)

def index(request):
    return render(request, 'nagios_alerts/index.html', {})
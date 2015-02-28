from django.db import models
import json
#from django.utils import timezone


# https://nagios.corp.hostcomm.ru/nagios/cgi-bin/status.cgi?host=all&servicestatustypes=28&jsonoutput


class Servers(models.Model):
#    host_server_name
    host_server_name = models.CharField(max_length=200)
    carrot = models.CharField(max_length=200)
    focus = models.CharField(max_length=200)

    def __str__(self):
        return self.host_server_name



#хуй знает что спарсить джсон запихать в базу

    # json_file='/home/anmakarov/Desktop/Projects/dashboard/nagios_alerts/nagios_out.json'
    # json_data=open(json_file)
    # data = json.load(json_data)


def a():
    FIELDS_MAP = {
        'host_name': 'host_server_name',
        'service_description': 'carrot',
        'status': 'focus'
    }

    data = json.loads(open('/home/anmakarov/Desktop/Projects/dashboard/nagios_alerts/nagios_out.json').read())
    for item in data['status ']['service_status']:
        server = Servers()
        for key, field in FIELDS_MAP.items():
            setattr(server, field, item[key])
        server.save()






# Create your models here.

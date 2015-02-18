from django.db import models
# import datetime
#from django.utils import timezone





class Servers(models.Model):
    host_server_name = models.CharField(max_length=200)

    def __str__(self):
        return self.host_server_name


# Create your models here.

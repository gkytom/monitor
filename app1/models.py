from django.db import models

# Create your models here.
class System(models.Model):
    sys_name = models.CharField(max_length=100)

class Machine(models.Model):
    hostname = models.CharField(max_length=100)
    procname = models.CharField(max_length=100)
    listen_port=models.IntegerField
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    system = models.ForeignKey(System,on_delete=models.SET_NULL)



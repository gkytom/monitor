from django.db import models

# Create your models here.
class System(models.Model):
    '''
    系统名表
    '''
    sys_name = models.CharField(max_length=100)
    def __str__(self):
        return self.sys_name

class Mode(models.Model):
    '''
    模块名表
    '''
    mod_name = models.CharField(max_length=100)
    def __str__(self):
        return self.mod_name

class Machine(models.Model):
    '''
    监控机器表
    '''
    hostname = models.CharField(max_length=100)
    procname = models.CharField(max_length=100)
    listen_port=models.IntegerField(default=0)
    created_time = models.DateTimeField()
    system = models.ForeignKey(System,on_delete=models.CASCADE)
    mode=models.ForeignKey(Mode,on_delete=models.CASCADE)

class api(models.Model):
    '''
    系统名表
    '''
    api_name = models.CharField(max_length=100)
    api_address = models.CharField(max_length=100)
    api_cycle=models.IntegerField(default=0)
    def __str__(self):
        return self.api_name,self.api_address







from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from app1.models import System,Mode,Machine
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'app1/shouye.html')
def apply_monitor(request):
    return render(request,'app1/monitor_push.html')

def add_data(request):
    '''
    将用户提交的数据写入数据库
    :param request:
    :return:
    '''
    '''
    获取监控项的所有信息
    '''
    if request.method == "GET":
        sysname = request.GET["sys_name"]
        modename= request.GET["mode_name"]
        hostname=request.GET["host_name"]
        proname=request.GET["proc_name"]
        createtime=request.GET["create_time"]
        '''
            所属系统信息
        '''
        try:
            if len(System.objects.filter(sys_name=sysname))==0:
                system = System()
                system.sys_name = sysname
                system.save()
                print('新的数据添加完成')
            else:
                print('重复数据无需添加')
        except:
            print('获取系统名失败')
        '''
        所屬模塊信息
        '''
        try:
            if len(Mode.objects.filter(mod_name=modename))==0:
                mode = Mode()
                mode.mod_name = modename
                mode.save()
                print('新的数据添加完成')
            else:
                print('重复数据无需添加')
        except:
            print('获取系统名失败')

    else:
        sysname = request.GET["sys_name"]
        modename = request.GET["mode_name"]
        hostname = request.GET["host_name"]
        proname = request.GET["proc_name"]
        createtime = request.GET["create_time"]






    return HttpResponseRedirect('/addok/')

def addok(request):
    return render(request,'app1/addok.html')

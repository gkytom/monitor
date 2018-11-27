from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from app1.models import System,Mode,Machine,api
from django.http import HttpResponseRedirect
import requests
import threading
import time
from django.views.decorators.cache import cache_page


def index(request):
    api_num=len(api.objects.all())
    api_num_list = []
    api_num_fen = int((api_num + 2 - 1) / 2)
    for i in range(0, api_num_fen):
        api_num_list.append(i + 1)
    api_name=api.objects.all()[0:2]

    return render(request,'app1/shouye.html',locals())
def apply_monitor(request):
    return render(request,'app1/monitor_push.html')

def add_data(request):
    '''
    将用户提交的监控数据写入数据库
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
        '''
        主机表
        '''
        machine = Machine()
        machine.hostname = hostname
        machine.procname = proname
        machine.created_time = createtime
        machine.save()

    else:
        sysname = request.GET["sys_name"]
        modename = request.GET["mode_name"]
        hostname = request.GET["host_name"]
        proname = request.GET["proc_name"]
        createtime = request.GET["create_time"]
    return HttpResponseRedirect('/addok/')




class SubThread():
    data = {}
    def __init__(self):
        pass
    def check_status(self,api_address,api_cycle):
        '''
        通用接口检查函数
        :param api_address:API地址
        :return:
        '''
        while True:
            time.sleep(api_cycle)
            status = '未知'
            try:
                r = requests.get(str(api_address))
                ask_time = r.elapsed.total_seconds()
                print(r.elapsed.total_seconds())
                try:
                    if float(ask_time) < float(3.0):
                        print("接口请求未超时")
                        status = '健康'
                except:
                    print("接口超时")
                    status = '超时'
            except:
                print('获取接口时限失败')

            SubThread.data["key"] = status
            print(SubThread.data)
            return SubThread.data




@cache_page(60)
def findapi(request):
    '''
    刷新API状态函数,用多线程
    :param request:
    :return:
    '''
    api_name = api.objects.all()  # 获取全部字段信息
    api_cycle = api.objects.values("api_cycle")[len(api.objects.values("api_cycle"))-1]["api_cycle"]
    print(api_cycle)
    api_num = len(api.objects.all())
    api_num_list = []
    api_num_fen = int((api_num + 2 - 1) / 3)
    for i in range(0, api_num_fen):
        api_num_list.append(i + 1)
    api_sum = len(api.objects.values("api_address")) # API接口总数数组
    print('thread %s is running...' % threading.current_thread().name)
    thread_list = []
    for thread in range(api_sum):
        obj=SubThread()
        t_each = threading.Thread(target=obj.check_status, args=(api.objects.values("api_address")[thread]['api_address'],api_cycle,))
        thread_list.append(t_each)
    status_list=[]
    for t in range(0,len(thread_list)):
        thread_list[t].setDaemon(True)  # 设置为守护线程
        thread_list[t].start()
        thread_list[t].join()  # 在这个子线程完成运行之前，主线程将一直被阻塞
        status = SubThread.data["key"]
        obj_api_status=api.objects.get(id=t+1)
        obj_api_status.api_status=status
        obj_api_status.save()
        status_list.append(status)
        del SubThread.data["key"]

    '''将api状态写到status字段中'''

    print('接口信息为'+str(status_list))
    api_name = api.objects.all()[0:3]
    # return render(request, 'app1/fenyezhanshi.html/',locals())
    return render(request, 'app1/whole_api_show.html/', locals())






def add_api(request):
    '''
    API接口入库
    :param request:
    :return:
    '''
    if request.method == "GET":

        apiname = request.GET["api_name"]
        apiaddress= request.GET["api_address"]
        apicycle = request.GET["api_cycle"]

        '''获取接口响应时间'''
        try:
            r=requests.get(apiaddress)
            print(r.elapsed.total_seconds())
        except:
            print('获取接口时限失败')

        API = api()
        API.api_name = apiname
        API.api_cycle= apicycle
        try:
            if len(api.objects.filter(api_address=apiaddress))==0:
                API.api_address = apiaddress
                API.save()
                print('新的数据添加完成')
            else:
                print('重复数据无需添加')
        except:
            print('获取接口路径失败')
    else:
        apiname = request.GET["api_name"]
        apiaddress = request.GET["api_address"]

    return HttpResponseRedirect('/addok/')

def addok(request):

    return render(request,'app1/addok.html')

def fenye(request):
    api_num = len(api.objects.all())
    api_num_list = []
    api_num_fen = int((api_num + 2 -1)/2)
    for i in range(0, api_num_fen):
        api_num_list.append(i + 1)
    current_page = request.GET.get('page', 1)
    print('获取的分页数为：')
    print(current_page)
    # start = (int(current_page)-1)*10
    start = (int(current_page) - 1) * 2
    end = int(current_page)*2
    api_name  = api.objects.all()[start:end]
    return render(request,'app1/API.html',locals())

def find_api_show(request):
    api_num = len(api.objects.all())
    api_num_list = []
    api_num_fen = int((api_num + 2 - 1) / 3)
    for i in range(0, api_num_fen):
        api_num_list.append(i + 1)
    current_page = request.GET.get('page', 1)
    print('获取的分页数为：')
    print(current_page)
    # start = (int(current_page)-1)*10
    start = (int(current_page) - 1) * 3
    end = int(current_page) * 3
    api_name = api.objects.all()[start:end]
    return render(request, 'app1/whole_api_show.html', locals())

def shouye(request):
    return render(request,'app1/menhu.html')
def ECS(request):
    return render(request,'app1/ECS.html')
def ECSapply(request):
    return render(request,'app1/ECSapply.html')
def controltable(request):
    return render(request,'app1/controltable.html')

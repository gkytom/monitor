from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^appl/$', views.apply_monitor, name='apply_monitor'),
    url(r'^addmonitor/$', views.add_data, name='add_data'),
    url(r'^addok/$', views.addok, name='addok'),
]
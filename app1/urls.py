from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addmonitor/$', views.add_data, name='add_data'),
    url(r'^addapi/$', views.add_api, name='add_api'),
    url(r'^find_api/$', views.findapi, name='find_api'),
    url(r'^check_status/$', views.SubThread().check_status, name='check_status'),
    url(r'^addok/$', views.addok, name='addok'),
]
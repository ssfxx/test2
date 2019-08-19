"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from testapp.views import about,disp_detail,list,index,add,test

urlpatterns = [
    url(r'^about/$',about),
    url(r'^list/([0-9a-zA-Z]+)/$',disp_detail),
    url(r'^list/$',list),
    url(r'^$',index),
    url(r'^about/(\d+)/(\d+)/$',add),
    url(r'^about/page=(?P<page>\d+)&sys=(?P<sys>\d+)&no=(?P<no>\d+)&next=(?P<next>\d+)$',test),
    path(r'^admin/', admin.site.urls),
]

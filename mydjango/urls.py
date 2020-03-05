"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path,include
from django.views.static import serve
from myapp.views import myindex,Myview,Adduser,search_post,list_modify,list_delete,update_post,Register

urlpatterns = [
    #定义超链接路由
    re_path('^static/upload/(?P<path>.*)$',serve,{'document_root':'/static/upload/'}),
    path('index/',Myview.as_view()),
    path('adduser/',Adduser.as_view()),
    path('post_user/',search_post),
    path('post_use/',update_post),
    path('register/',Register.as_view()),

    re_path(r'^list_modify/(?P<i_id>\w+)/$',list_modify,name='list_modify'),
    re_path(r'^list_delete/(?P<i_id>\w+)/$',list_delete,name='list_delete'),


]

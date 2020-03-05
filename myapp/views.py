from django.shortcuts import render,redirect
#导包
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
#导入类视图
from django.views import View

from .models import *
#from myapp.models import User
import json
from django.core.serializers import serialize
from rest_framework.response import Response
from rest_framework.views import APIView
#导入加密库
import hashlib
#导入图片库
#绘画库
from PIL import ImageDraw
#字体库
from PIL import ImageFont
#图片库
from PIL import Image
#随机库
import random
#文件流
import io

import requests

#导入上传文件夹配置
from mydjango.settings import UPLOAD_ROOT
import os

#导入原生sql模块
from django.db import connection

import jwt

#导入redis数据库
import redis

#导入时间模块
import time

#导入公共目录变量
from mydjango.settings import BASE_DIR

#导包
from django.db.models import Q,F

#导入dwebsocket的库
from dwebsocket.decorators import accept_websocket
import uuid

#方法视图
def myindex(request):

    return HttpResponse('这里是首页')

class Adduser(View):
    def get(self,request):

        return render(request,'test.html')

class Myview(View):

    def get(self,request):
        list=[]
        user=User.objects.all()
        for i in user:
            list.append({
                'name':i.username,
                'password':i.password,
                'time':i.create_time
            })
        return render(request,'index.html',locals())


def search_post(request):

        user = request.POST.get('username')
        password = request.POST.get('password')
        print(user, password)
        User.objects.create(username=user,password=password)
        return HttpResponse('添加成功')



def list_modify(request,i_id):
    print(i_id)
    User.objects.filter(username=i_id).delete()
    return HttpResponse('删除成功')





def list_delete(request,i_id):
    print(i_id)
    name=i_id

    return render(request,'update.html',locals())

def update_post(request):
    user = request.POST.get('username')
    password = request.POST.get('password')
    print(user, password)
    User.objects.filter(username=user).update(password=password)
    return HttpResponse('修改成功')
def make_password(mypass):
    # 生成md5对象
    md5=hashlib.md5()
    #  定义随机对象
    sign_str=str(mypass)
    # 转码
    sign_utf8=sign_str.encode(encoding='utf-8')
    #  加密
    md5.update(sign_utf8)
    # 生成秘钥字符串
    md5_server=md5.hexdigest()

    return md5_server


class Register(View):
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=User.objects.filter(username=username).first()
        if user:
            res={}
            res['code']=405
            res['message']='该用户名已存在'
            return HttpResponse(json.dumps(res))
        else:
            user=User(username=username,password=password)
            user.save()
            res = {}
            res['code'] = 200
            res['message'] = '注册成功'
            return HttpResponse(json.dumps(res))


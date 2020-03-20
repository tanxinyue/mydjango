from django.shortcuts import render,redirect
#导包
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
#导入类视图
from django.utils.decorators import method_decorator
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
from myapp.models import *
from myapp.myser import UserSerializer,PicsSerializer
#导入上传文件夹配置
from mydjango.settings import UPLOAD_ROOT
import os

#导入原生sql模块
from django.db import connection

import jwt
#
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
#  导包
import redis
#  定义ip地址和端口
host='127.0.0.1'
port=6379
#简历redis对象
# r=redis.Redis(host=host,port=port)
from myapp.models import User


#定义七牛云存储接口
from qiniu import Auth
class Qiniukaoshi(APIView):
    def get(self,request):
        #定义秘钥
        q=Auth('p1YCAtlMQydBxWfKF45Wuf_Cqb41JTeJFIAGW2S9','chE4ioNSPRy7VFzV33okYbb4kDyqu-OXqbW6Xqoj')
        #指定上传空间
        token=q.upload_token('atmyfileupload')
        print(token)
        res={}
        res['token']=token
        return Response(res)


# 装饰器的使用

def my_decorator(func):
    def wrapper(request,*args,**kwargs):
        print('这个装饰器被调用了')
        print('请求接口，地址是:%s' % request.path)
        uid = request.GET.get('uid')
        jwt1 = request.GET.get('jwt',None)
        decode_jwt = jwt.decode(jwt1, '123', algorithms=['HS256'])
        if decode_jwt['uid'] != str(uid):
            return HttpResponse('你篡改了用户的id')

        return func(request,*args,**kwargs)
    return wrapper


#用户信息类
class Userinfokaoshi(APIView):
    @method_decorator(my_decorator)
    def get(self,request):
        uid=request.GET.get('uid')
        #查询数据
        user=User.objects.get(id=int(uid))
        #序列化对象
        user_ser=UserSerializer(user)
        return Response(user_ser.data)

class Updateuser(APIView):
    def get(self,request):
        img=request.GET.get('img')
        uid=request.GET.get('uid')
        #查询数据
        user=User.objects.get(id=int(uid))
        user.img=img
        user.save()
        return Response({'code':200,'message':'更新成功'})

class Movieinfo(APIView):
    def post(self,request):
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        print(title,desc)
        return HttpResponse(json.dumps({'title':title,'desc':desc}))




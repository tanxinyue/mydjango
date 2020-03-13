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
#  导包
import redis
#  定义ip地址和端口
host='127.0.0.1'
port=6379

#简历redis对象

r=redis.Redis(host=host,port=port)


# 注册
class Register(View):
    def post(self,request):
        # 获取前端穿过的参数
        username=request.POST.get('username')
        password=request.POST.get('password')
        code=request.POST.get('code')
        print(username,password,code)
        # 存到redis中
        redis_code=r.get('code')
        redis_code=redis_code.decode('utf-8')
        s_code=request.session.get('code')
        print('session',s_code)
        print(redis_code)
        # 判断前端穿过的验证码,和redis中的验证码是否一致
        if code!=redis_code:
            res = {}
            res['code'] = 405
            res['message'] = '验证码输入错误，请重新输入'
            return HttpResponse(json.dumps(res))
        user = User.objects.filter(username=username).first()
        #判断该用户是否存在
        if user:
            res = {}
            res['code'] = 405
            res['message'] = '该用户名已存在'
            return HttpResponse(json.dumps(res))
        #如果不存在，注册成功
        else:
            user = User(username=username, password=password)
            user.save()
            res = {}
            res['code'] = 200
            res['message'] = '注册成功'
            return HttpResponse(json.dumps(res))


#登录
class  Login(View):
    def post(self,request):
        # 获取前端传过来的参数
        username=request.POST.get('username','null')
        password=request.POST.get('password','null')
        print(username,password)
        #判断用户表中是否有该用户
        user=User.objects.filter(username=username,password=password).first()
        # 如果存在登录成功
        if user:
            res = {}
            res['code'] = 200
            res['message'] = '登录成功'
            res['username'] = user.username
            res['uid'] = user.id
            return HttpResponse(json.dumps(res))
        #如果没有,提示用户名或者密码错误
        else:
            res = {}
            res['code'] = 405
            res['message'] = '用户名密码错误'
            return HttpResponse(json.dumps(res))

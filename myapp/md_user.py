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
from mydjango.settings import UPLOAD_ROOT

class UploadFile(View):
    def post(self,request):
        # 接收参数
        img1 = request.FILES.get('file')
        username = request.POST.get('username')
        print(username)
        print(img1)
        print(img1.name)
        # 建立文件流对象
        f = open(os.path.join(UPLOAD_ROOT, '', img1.name), 'wb')
        # 写入服务器
        for chunk in img1.chunks():
            f.write(chunk)
        f.close()
        # 存储到用户头像字段
        User.objects.filter(username=username).create(img=img1)
        #拿到图片添加水印

        img = Image.open('./static/upload/'+img1.name)
        # 生成画笔
        draw = ImageDraw.Draw(img)
        # 定义字体
        my_font = ImageFont.truetype(font='c:\\Windows\\Fonts\\msyh.ttc', size=40)
        # 打水印
        draw.text((20, 20), username, fill=(76, 234, 124, 180), font=my_font)
        # 查看图片
        # img.show()
        # 有水印图片的名称

        # 存储图片
        img.save('./static/upload/'+img1.name)
        # 返回文件名
        return HttpResponse(json.dumps({'filename': img1.name}, ensure_ascii=False),
                            content_type='application/json')



class Update(View):
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        User.objects.filter(username=username).update(password=password)

        return HttpResponse(json.dumps({'code':200}))



#定义七牛云存储接口
from qiniu import Auth
class Qiniu(APIView):
    def get(self,request):
        #定义秘钥
        q=Auth('p1YCAtlMQydBxWfKF45Wuf_Cqb41JTeJFIAGW2S9','chE4ioNSPRy7VFzV33okYbb4kDyqu-OXqbW6Xqoj')
        #指定上传空间
        token=q.upload_token('atmyfileupload')
        print(token)
        res={}
        res['token']=token
        return Response(res)

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

r=redis.Redis(host=host,port=port)



class InsertPics(APIView):
    def post(self,request):
        img = request.FILES.get('file')
        title = request.POST.get('title')
        link = request.POST.get('link')

        # 建立文件流对象
        f = open(os.path.join(UPLOAD_ROOT, '', img.name), 'wb')
        # 写入服务器
        for chunk in img.chunks():
            f.write(chunk)
        f.close()

        # 写入服务器

        pics=Pics.objects.filter(title=title).first()
        if pics:
            res={}
            res['code']=405
            res['message']='该活动已存在'
            return  Response(res)
        else:
            pics=Pics(title=title,link=link,img=img)
            pics.save()
            res = {}
            res['code'] = 200
            res['message'] = '添加成功'


            return Response(res)
#
#
class DeletePics(APIView):
    def post(self,request):

        title = request.POST.get('title')

        print(title)

        pics=Pics.objects.filter(title=title).first()
        if pics:
            Pics.objects.filter(title=title).delete()
            res={}
            res['code']=200
            res['message']='删除成功'
            return  Response(res)
        else:
            res = {}
            res['code'] = 405
            res['message'] = '该幻灯片不存在'


            return Response(res)

class Showpics(APIView):
    def get(self,request):
        all = Pics.objects.all()
        res={}
        list = []
        for i in all:
            list.append({
                'id':i.id,
                'title': i.title,
                'link': i.link,
                'image': i.img
            })

        res['list'] = list
        return Response(res)


class UpdatePics(APIView):
    def post(self, request):
        id=request.POST.get('cid')


        title = request.POST.get('title')
        link = request.POST.get('link')
        img = request.FILES.get('img')
        print(id,title,link,img)
        f = open(os.path.join(UPLOAD_ROOT, '', img.name), 'wb')
        # 写入服务器
        for chunk in img.chunks():
            f.write(chunk)
        f.close()
        Pics.objects.filter(pk=id).update(title=title,link=link,img=img)
        res={}
        res['code']=200
        res['message']='修改成功'
        return Response(res)


from django.shortcuts import render,redirect
#导包
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
#导入类视图
from django.views import View

from mydjango import settings
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
#
#导入redis数据库
import redis

#导入时间模块
import time

#导入公共目录变量
from mydjango.settings import BASE_DIR

#导包
from django.db.models import Q,F
import datetime
#导入dwebsocket的库
from dwebsocket.decorators import accept_websocket
import uuid
#  导包
import redis
#  定义ip地址和端口
host='127.0.0.1'

port=6379


# 定义连接对象

r=redis.Redis(host=host,port=port)

#某个商品取消关注
class kaoshiCancelFlow(APIView):
    def get(self, request):
        gid = request.GET.get('gid', None)
        uid = request.GET.get('uid', None)
        time = r.ttl('myrank')
        if time != 0:
            res = {}
            res['code'] = 403
            res['message'] = '请稍后重试'
            return Response(res)

        result=UserFlow.objects.filter(gid=gid, uid=uid).first()
        if result:
            r.zadd('myrank', {'gid': gid, 'uid': uid})
            # 设置过期时间180s
            r.expire('myrank', 180)

            UserFlow.objects.filter(gid=gid, uid=uid).delete()
            res = {}
            res['code'] = 200
            res['message'] = '取消收藏成功'
            return Response(res)
        else:
            res = {}
            res['code'] = 403
            res['message'] = '您还未收藏该商品'
            return Response(res)

#进行商品收藏
class kaoshiGoodflow(APIView):
    def get(self, request):
        gid = request.GET.get('gid', None)
        uid = request.GET.get('uid', None)
        time=r.ttl('myrank')
        if time!=0:
            res = {}
            res['code'] = 403
            res['message'] = '请稍后关注'
            return Response(res)

        result=UserFlow.objects.filter(gid=gid,uid=uid).first()
        if result:
            res = {}
            res['code'] = 403
            res['message'] = '该商品已经在收藏列表中'
            return Response(res)
        else:
            UserFlow.objects.create(uid=uid,gid=gid)
            r.zadd('myrank', {'gid': gid,'uid':uid})
            #设置过期时间180s
            r.expire('myrank',180)

            res = {}
            res['code'] = 200
            res['message'] = '收藏成功'
            return Response(res)



from myapp.myser import GoodsSerializer


class kaoshiShowGoodsList(APIView):
    def get(self,request):
        #当前页
        page=int(request.GET.get('page',1))
        # 一页有多少条商品
        size=int(request.GET.get('size',1))
        #定义从哪开始切换
        data_start=(page-1)*size
        # 定义切到哪里
        data_end=page*size
        #查询数据
        goodslist=Goods.objects.all()[data_start:data_end]
        #查询总数量
        count=Goods.objects.count()
        #序列化操作
        goods_ser=GoodsSerializer(goodslist,many=True)
        # 返回数据
        res={}
        res['total']=count
        res['data']=goods_ser.data
        return Response(res)



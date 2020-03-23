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

from myapp.myser import GoodsSerializer


class InsertGoods(APIView):
    def post(self,request):
        name = request.POST.get('name','null')
        desc = request.POST.get('desc','null')
<<<<<<< HEAD
        parms = request.POST.get('parms','null')
        price = request.POST.get('price','null')
        cate_id = request.POST.get('cate_id','null')
        image = request.FILES.get('img')
        video = request.FILES.get('video')
        print(name, desc, price, cate_id,parms,image,video)

=======
        color = request.POST.get('color','null')
        size = request.POST.get('size','null')
        price = request.POST.get('price','null')
        cate_id = request.POST.get('cate_id','null')
        print(name, desc, price, cate_id, color,size)
        parms=dict()
        parms['color']=color
        parms['size']=size
        print(json.dumps(parms))
>>>>>>> 2a52acabbcd8b7f0cb50cc8d3a14b35d2fc50bf6

        goods=Goods.objects.filter(name=name).first()

        if goods:
            res={}
            res['code']=405
            res['message']='该商品已经存在'
            return  Response(res)
        else:
<<<<<<< HEAD
            goods=Goods(name=name,desc=desc,cate_id=cate_id,price=price,parms=parms,img=image,video=video)
=======
            goods=Goods(name=name,desc=desc,cate_id=cate_id,price=price,parms=json.dumps(parms))
>>>>>>> 2a52acabbcd8b7f0cb50cc8d3a14b35d2fc50bf6
            goods.save()
            f = open(os.path.join(settings.UPLOAD_ROOT, image.name), 'wb')
            for i in image.chunks():
                f.write(i)
            f.close()
            res = {}
            res['code'] = 200
            res['message'] = '添加成功'
            r.set('parms', json.dumps(parms))
            return Response(res)

# 商品列表页
class GoodsList(APIView):
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



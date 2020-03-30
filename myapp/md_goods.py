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
import pymongo #导包
client = pymongo.MongoClient(host='127.0.0.1',port=27017) #链接mongodb
#  导包
import redis
#  定义ip地址和端口
host='127.0.0.1'
port=6379
#评论展示
class Showcomment(APIView):
    def get(self,request):
        #获取商品id
        id=request.GET.get('id',None)
        #查询评论
        comment=Comment.objects.filter(gid=int(id)).order_by('-id')
        #序列化
        comment_ser=CommentSerializer(comment,many=True)
        return Response(comment_ser.data)




import copy
#反序列化入库
#商品评论
from myapp.myser import CommentSerializer
class InsertComment(APIView):
    def post(self,request):
        #mongo存储
        params = copy.deepcopy(request.data)
        # 建立数据库对象
        db = client.md
        # 建立表对象
        table = db.content
    


        table.insert({"gid":params['gid'] , "content":params['content'],'uid':params['uid']})



        #初始化参数
        comment=CommentSerializer(data=request.data)

        #数据校验
        if comment.is_valid():
            #数据入库
            comment.save()
        return Response({'code':200,'message':'入库成功'})



class Shoponline(APIView):
    def get(self,request):
        # 获取客户ip
        if 'HTTP_x_FORWARDED_FOR' in request.META:
            ip=request.META.get('HTTP_x_FORWARDED_FOR')
        else:
            ip=request.META.get('REMOTE_ADDR')

        #对用户ip进行存储
        r.sadd('shoponline',ip)
        #设置超时时间,超时单位秒
        r.expire('shoponline',60)
        #获取在线人数的数量
        olinenum=r.smembers('shoponline')
        return Response({'allnum':len(olinenum)})

#简历redis对象
#统计在线人数
class Getonline(APIView):
    def get(self,request):
        # 获取客户ip
        if 'HTTP_x_FORWARDED_FOR' in request.META:
            ip=request.META.get('HTTP_x_FORWARDED_FOR')
        else:
            ip=request.META.get('REMOTE_ADDR')

        #对用户ip进行存储
        r.sadd('online',ip)
        #设置超时时间,超时单位秒
        r.expire('online',20)
        #获取在线人数的数量
        olinenum=r.smembers('online')
        return Response({'allnum':len(olinenum)})






r=redis.Redis(host=host,port=port)
from mydjango.settings import UPLOAD_ROOT
from bson import json_util as bjson
from myapp.myser import GoodsSerializer
class Updatetags(APIView):
    def get(self,request):
        id = request.GET.get('id', None)
        tags = request.GET.get('tags', None)
        tag = tags.split(",")
        # 建立数据库对象
        db = client.md
        # 建立表对象
        table = db.mytag
        # 排重操作
        table.update_one({'gid': str(id)},{'$set':{'tags':tag}})
        res = {}
        res['code'] = 200
        res['message'] = '标签修改成功'
        return Response(res)




class updateGoods(APIView):
    def get(self,request):
        name = request.GET.get('name','null')
        # content = request.GET.get('content','null')

        parms = request.GET.get('parms','null')
        price = request.GET.get('price','null')
        cate_id = request.GET.get('cate_id','null')
        id=request.GET.get('id','null')

        print(name,parms,price,id)
        Goods.objects.filter(id=id).update(name=name,parms=parms,price=price,cate_id=cate_id)
        res = {}
        res['code'] = 200
        res['message'] = '修改成功'
        return Response(res)



#获取商品标签
class GetTags(View):
    def get(self,request):
        id = request.GET.get('id', None)
        # 建立数据库对象
        db = client.md
        # 建立表对象
        table = db.mytag
        #查询数据
        res=table.find_one({"gid":str(id)})
        return HttpResponse(bjson.dumps(res,ensure_ascii=False))


class InsertTags(APIView):
    def post(self,request):
        id = request.POST.get('id', None)
        tags = request.POST.get('tags', None)
        print(1111111,id,tags)

        tag=tags.split(",")

        #建立数据库对象
        db=client.md
        #建立表对象
        table=db.mytag
        #排重操作
        res=table.find({'gid':str(id)}).count()
        print(res)
        if res>0:
            return Response({'message':'重复数据'})
        else:
            #入库操作
            table.insert({"gid":str(id),"tags":tag})
            return Response({'message':'入库成功'})


class InsertGoods(APIView):
    def post(self,request):
        name = request.POST.get('name','null')
        desc = request.POST.get('desc','null')

        parms = request.POST.get('parms','null')
        price = request.POST.get('price','null')
        cate_id = request.POST.get('cate_id','null')
        image = request.FILES.get('img')

        print(name, desc, price, cate_id,parms,image)
        goods=Goods.objects.filter(name=name).first()

        if goods:
            res={}
            res['code']=405
            res['message']='该商品已经存在'
            return  Response(res)
        else:

            goods=Goods(name=name,desc=desc,cate_id=cate_id,price=price,parms=parms,img=image)
            goods.save()
            f = open(os.path.join(settings.UPLOAD_ROOT, image.name), 'wb')
            for i in image.chunks():
                f.write(i)
            f.close()
            goodsx=Goods.objects.filter(name=name).first()
            res = {}
            res['code'] = 200
            res['message'] = '添加成功'
            res['id']=goodsx.id

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



# 商品信息接口
class GoodInfo(APIView):
    def get(self,request):
        id = int(request.GET.get('id'))
        print(id)
        good = Goods.objects.get(pk=id)
        goods_ser = GoodsSerializer(good)
        return Response(goods_ser.data)



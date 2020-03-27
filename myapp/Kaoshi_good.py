from mydjango import settings
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
#导入上传文件夹配置
from mydjango.settings import UPLOAD_ROOT
import os
from myapp.myser import KsGoodsSerializer #导入商品序列化
import pymongo #导包
client = pymongo.MongoClient(host='127.0.0.1',port=27017) #链接mongodb
# 商品列表页
class KaoshiGoodsList(APIView):
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
        goodslist=KaoshiGoods.objects.all()[data_start:data_end]
        #查询总数量
        count=KaoshiGoods.objects.count()
        #序列化操作
        goods_ser=KsGoodsSerializer(goodslist,many=True)
        # 返回数据
        res={}
        res['total']=count
        res['data']=goods_ser.data
        return Response(res)



class KaoshiInsertTags(APIView):
    def post(self,request):
        id = request.POST.get('id', None) #
        tags = request.POST.get('tags', None)
        tag=tags.split(",")

        #建立数据库对象
        db=client.kaoshi
        #建立表对象
        table=db.kaoshitag
        #排重操作
        res=table.find({'gid':str(id)}).count()
        print(res)
        if res>0:
            return Response({'message':'重复数据'})
        else:
            #入库操作
            table.insert({"gid":str(id),"tags":tag})
            return Response({'message':'入库成功'})


class KaoshiInsertGoods(APIView):
    def post(self, request):
        # 获取数据
        name = request.POST.get('name', 'null')
        desc = request.POST.get('desc', 'null')
        parms = request.POST.get('parms', 'null')
        price = request.POST.get('price', 'null')
        cate_id = request.POST.get('cate_id', 'null')
        image = request.FILES.get('img')
        #进入查询，判断商品是否存在
        goods = KaoshiGoods.objects.filter(name=name).first()
        # 如果存在提示商品已经存在
        if goods:
            res = {}
            res['code'] = 405
            res['message'] = '该商品已经存在'
            return Response(res)
        # 否则数据入库，返回信息给前端
        else:

            goods = KaoshiGoods(name=name, desc=desc, cate_id=cate_id, price=price, parms=parms, img=image)
            goods.save()
            f = open(os.path.join(settings.UPLOAD_ROOT, image.name), 'wb')
            for i in image.chunks():
                f.write(i)
            f.close()
            goodsx = KaoshiGoods.objects.filter(name=name).first()
            res = {}
            res['code'] = 200
            res['message'] = '添加成功'
            res['id'] = goodsx.id
            return Response(res)
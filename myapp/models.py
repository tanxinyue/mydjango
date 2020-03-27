from django.db import models
from datetime import datetime
from django.utils import timezone
class Base(models.Model):
    create_time=models.DateTimeField(default=timezone.now,null=True)
    class Meta:
        abstract=True



class Cate(Base):
    name=models.CharField(max_length=200)
    cid=models.IntegerField()

class User(Base):
    username=models.CharField(max_length=60,verbose_name='用户名')
    password=models.CharField(max_length=120,verbose_name='密码')
    # 头像
    img = models.CharField(max_length=200)
    # 类别  0普通用户 1超级管理员
    type = models.IntegerField(default=0, null=True)
    class Meta:
        db_table='user'

#幻灯片
class Pics(Base):
    #名称
    title=models.CharField(max_length=200)
    #链接
    link=models.CharField(max_length=200)
    #图片
    img=models.CharField(max_length=200)
    class Meta:
        db_table='pics'

class Goods(Base):
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    parms=models.CharField(max_length=500)
    img=models.CharField(max_length=200,null=True)
    video=models.CharField(max_length=200,null=True)
    price=models.IntegerField()
    flow=models.IntegerField(default=0,null=True)
    cate_id=models.IntegerField()
    class Meta:
        db_table='goods'



class KaoshiGoods(Base):
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    parms=models.CharField(max_length=500)
    img=models.CharField(max_length=200,null=True)

    price=models.IntegerField()
    flow=models.IntegerField(default=0,null=True)
    cate_id=models.IntegerField()
    class Meta:
        db_table='kaoshigood'


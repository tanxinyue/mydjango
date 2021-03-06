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

#定义验证码的类
class MyCode(View):
    #定义随机颜色
    def get_random_color(self):
        R=random.randrange(255)
        G=random.randrange(255)
        B=random.randrange(255)
        return (R,G,B)
    #获取验证码视图
    def get(self,request):
        #画布
        img_size=(120,50)
        #定义画图对象
        image=Image.new('RGB',img_size,'white')
        #定义画笔对象
        draw=ImageDraw.Draw(image,'RGB')
        #定义随机字符串
        num='0123456789'
        #容器
        code_str=''
        #定义字体
        font_size=ImageFont.truetype(font='C:\\Windows\\Fonts\\Arial.ttf',size=15)
        for i in range(4):
            #  获取随机颜色
            text_color=self.get_random_color()
            #获取随机字符串长度
            ran_num=random.randrange(len(num))
            #获取字符集
            random_str=num[ran_num]
            #添加到容器中
            code_str+=random_str
            #将字符串添加到画布上
            draw.text((10+30*i,20),random_str,text_color,font=font_size)
        #简历缓存区
        buf=io.BytesIO()
        #将验证码保存到redis中
        r.set('code',code_str)
        request.session['code']=code_str
        #保存图片
        image.save(buf,'png')
        return HttpResponse(buf.getvalue(),'image/png')














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
        code=request.POST.get('code')
        print(username,password,code)
        redis_code=r.get('code')
        redis_code=redis_code.decode('utf-8')
        s_code=request.session.get('code')
        print('session',s_code)
        print(redis_code)
        if code!=redis_code:
            res = {}
            res['code'] = 405
            res['message'] = '验证码输入错误，请重新输入'
            return HttpResponse(json.dumps(res))




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


class  Login(View):
    def post(self,request):
        username=request.POST.get('username','null')
        password=request.POST.get('password','null')
        print(username,password)
        user=User.objects.filter(username=username,password=password).first()
        if user:
            res = {}
            encode_jwt = jwt.encode({'uid': str(user.id)}, '123', algorithm='HS256')
            encode_str = str(encode_jwt, 'utf-8')
            res['jwtpass'] = encode_str
            res['code'] = 200
            res['message'] = '登录成功'
            res['username'] = user.username
            res['uid'] = user.id
            res['type']=user.type
            #加入jwt令牌机制

            return HttpResponse(json.dumps(res))
        else:
            res = {}
            res['code'] = 405
            res['message'] = '用户名密码错误'
            return HttpResponse(json.dumps(res))


# def wb_back(request):
#     code=request.GET.get('code')
#     access_token_url='https://api.weibo.com/oauth2/access_token'
#     res=requests.post(access_token_url,data={'client_id':'1990796315','client_secret':'4f3357bc1f3c89a000fd452c2702aa3e','grant_type':'authorization_code','code':code,'redirect_uri':'http://127.0.0.1:8000/my_weibo'})
#
#     print(res)
#     res=json.loads(res.text)
#     print(res)
#
#
#     return HttpResponse('授权成功')



class wb_back(View):
    def post(self,request):
        code = request.POST.get('code')
        print(code)
        params = {
            'client_id': '2144764739',
            'client_secret': 'e72238ce0f2e5792ecc14badc0367fe6',
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://127.0.0.1:8080/my_weibo',

        }
        access_token_url='https://api.weibo.com/oauth2/access_token'
        res=requests.post(url=access_token_url,data=params)
        print(res.text)
        res1 = json.loads(res.text)
        result=requests.get('https://api.weibo.com/2/users/show.json',params={'access_token':res1['access_token'],'uid':res1['uid']})
        res2=json.loads(result.text)
        print(res2['name'])
        #判断该用户是否曾经登录过
        user=User.objects.filter(username=str(res2['name'])).first()
        sina_id=''
        user_id=''
        if user:
            sina_id=user.username
            user_id=user.id
        else:
            #手动创建账号
            user=User(username=str(res2['name']),password='')
            user.save()
            sina_id=res2['name']
            #查询刚才入库的新账号id
            user=User.objects.filter(username=str(res2['name'])).first()
            user_id=user.id







        return HttpResponse(json.dumps({'username':sina_id,'uid':user_id}))

        # return redirect("http://127.0.0.1:8080?sina_id=" + sina_id + "&uid=" + str(user_id))




#构造钉钉登录url
def ding_url(request):
    appid = 'dingoa5ckwctqpp3eiuw4e'
    redirect_uri = 'http://127.0.0.1:8000/dingding_back'

    return redirect('https://oapi.dingtalk.com/connect/qrconnect?appid='+appid+'&response_type=code&scope=snsapi_login&state=STATE&redirect_uri='+redirect_uri)


import time
import hmac
import base64
from hashlib import sha256
import urllib
import json

#构造钉钉回调方法
def ding_back(request):

    #获取code
    code = request.GET.get("code")

    t = time.time()
    #时间戳
    timestamp = str((int(round(t * 1000))))
    appSecret ='0R8zFyX2GHEwf-nEkbmDkhpv-3jfUHDgTFzOeaLd7yDIHSDjOAnMJGAFQfDBK3Ry'
    #构造签名
    signature = base64.b64encode(hmac.new(appSecret.encode('utf-8'),timestamp.encode('utf-8'), digestmod=sha256).digest())
    #请求接口，换取钉钉用户名
    payload = {'tmp_auth_code':code}
    headers = {'Content-Type': 'application/json'}
    res = requests.post('https://oapi.dingtalk.com/sns/getuserinfo_bycode?signature='+urllib.parse.quote(signature.decode("utf-8"))+"&timestamp="+timestamp+"&accessKey=dingoa5ckwctqpp3eiuw4e",data=json.dumps(payload),headers=headers)

    res_dict = json.loads(res.text)
    print(res_dict)
    print(res_dict['user_info']['nick'])
    d_username=res_dict['user_info']['nick']
    user = User.objects.filter(username=d_username).first()
    ding_id = ''
    user_id = ''
    #判断是否存在
    if user:
       ding_id = user.username
       user_id = user.id
    else:
        # 手动创建账号
        user = User(username=d_username, password='')
        user.save()
        ding_id = d_username
        # 查询刚才入库的新账号id
        user = User.objects.filter(username=d_username).first()
        user_id = user.id

    return redirect("http://127.0.0.1:8080/finish?ding_id=" + ding_id + "&uid=" + str(user_id))
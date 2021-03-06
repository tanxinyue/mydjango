"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.views.static import serve
from myapp.views import myindex,Myview,Adduser,search_post,list_modify,list_delete,update_post,\
    Register,MyCode,Login,wb_back,ding_url,ding_back
from myapp.md_user import UploadFile,Update,Qiniu,Updateuser,Userinfo
from myapp.md_pics import InsertPics,Showpics,DeletePics,UpdatePics

from myapp.md_goods import GoodsList,Shoponline,UidFlow,Goodflow,UsershowFlow,CancelFlow,AllCancelFlow

from myapp.md_goods import InsertGoods,GoodInfo,InsertTags,GetTags,updateGoods,Updatetags,Getonline
from myapp.md_goods import InsertComment,Showcomment,UserList,CommentsList,Rediscount
from myapp.kaoshi02 import Qiniukaoshi,Updateuser,Userinfokaoshi,Movieinfo
from myapp.Kaoshi_good import KaoshiInsertGoods,KaoshiInsertTags,KaoshiGoodsList
from myapp.kaoshi0403 import  kaoshiCancelFlow,kaoshiGoodflow
from myapp.md_goods import Goodsrange,GoodRank,GoodsSearch
urlpatterns = [
    #定义超链接路由
    re_path('^static/upload/(?P<path>.*)$',serve,{'document_root':'/static/upload/'}),
    path('index/',Myview.as_view()),
    path('adduser/',Adduser.as_view()),
    path('post_user/',search_post),
    path('post_use/',update_post),
    path('register/',Register.as_view()),
    path('code/',MyCode.as_view()),
    path('login/',Login.as_view()),
    path('user_login/',wb_back.as_view()),
    path('ding_url/',ding_url),
    path('dingding_back/',ding_back),
    path('uploadfile/',UploadFile.as_view()),
    path('update/',Update.as_view()),
    path('uptoken/',Qiniu.as_view()),
    path('updateuser/',Updateuser.as_view()),
    path('userinfo/',Userinfo.as_view()),
    path('pics/',InsertPics.as_view()),
    path('showpics/',Showpics.as_view()),
    path('dpics/',DeletePics.as_view()),
    path('upics/',UpdatePics.as_view()),
    path('insertgoods/',InsertGoods.as_view()),
    path('goodinfo/',GoodInfo.as_view()),
    path('inserttags/',InsertTags.as_view()),
    path('gettags/',GetTags.as_view()),
    path('upgoods/',updateGoods.as_view()),
    path('uptags/',Updatetags.as_view()),
    path('getoline/',Getonline.as_view()),
    path('shopoline/',Shoponline.as_view()),
    path('insertcommet/',InsertComment.as_view()),
    path('showcomment/',Showcomment.as_view()),
    path('uidflow/',UidFlow.as_view()),
    path('goodflow/',Goodflow.as_view()),
    path('peopleflow/',UsershowFlow.as_view()),
    path('disflow/',CancelFlow.as_view()),
    path('alldisflow/',AllCancelFlow.as_view()),
    path('redisflow/',Rediscount.as_view()),
    path('ksflow/',kaoshiGoodflow.as_view()),
    path('cancelflow/',kaoshiCancelFlow.as_view()),
    path('goodclick/',Goodsrange.as_view()),
    path('goodrank/',GoodRank.as_view()),
    path('search/',GoodsSearch.as_view()),

    path('goodslist/',GoodsList.as_view()),
    path('userlist/',UserList.as_view()),
    path('pagelist/',CommentsList.as_view()),


    path('kstoken/',Qiniukaoshi.as_view()),
    path('ksuserinfo/',Userinfokaoshi.as_view()),
    path('ksup/',Movieinfo.as_view()),
    path('ksaddgoods/',KaoshiInsertGoods.as_view()),
    path('ksaddtags/',KaoshiInsertTags.as_view()),
    path('ksgoodlist/',KaoshiGoodsList.as_view()),



    re_path(r'^list_modify/(?P<i_id>\w+)/$',list_modify,name='list_modify'),
    re_path(r'^list_delete/(?P<i_id>\w+)/$',list_delete,name='list_delete'),


]

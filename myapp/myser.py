#导包
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = "__all__"

class PicsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pics
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Goods
        fields = "__all__"

class KsGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model=KaoshiGoods
        fields = "__all__"

# 评论类的数列器
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = "__all__"

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


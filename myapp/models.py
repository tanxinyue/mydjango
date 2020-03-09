from django.db import models
from datetime import datetime
from django.utils import timezone
class Base(models.Model):
    create_time=models.DateTimeField(default=timezone.now,null=True)
    class Meta:
        abstract=True

class User(Base):
    username=models.CharField(max_length=60,verbose_name='用户名')
    password=models.CharField(max_length=120,verbose_name='密码')
    class Meta:
        db_table='user'
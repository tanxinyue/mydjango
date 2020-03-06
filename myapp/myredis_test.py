#  导包
import redis
#  定义ip地址和端口
host='127.0.0.1'

port=6379


# 定义连接对象

r=redis.Redis(host=host,port=port)
r.set('test','test')
mytest=r.get('test')
mytest=mytest.decode('utf-8')
print(mytest)
import redis

#定义地址和端口
host = '127.0.0.1'
port = 6379

#建立redis连接
r = redis.Redis(host=host,port=port)

# #声明一个值
# r.set('test','123')
#
# #取值
# code = r.get('test')
#
# #转码
# code = code.decode('utf-8')
#
# print(code)

#
#
# r.sadd('testtets','爆款')
# r.sadd('testtets','修身')
# #查询
# myset=r.smembers('testtets')
# print(myset)


# list的使用
r.lpush('testlist','1')
mylist=r.lrange('testlist',0,r.llen('testlist'))
print(mylist)

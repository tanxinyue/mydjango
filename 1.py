# #导包
import jwt

#进行编码

encode_jwt=jwt.encode({'uid':14},'123',algorithm='HS256')
print(encode_jwt)
#解码
# #强转
encode_str=str(encode_jwt,'utf-8')
decode_jwt=jwt.decode(encode_str,'123',algorithms=['HS256'])
print(decode_jwt)

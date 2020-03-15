from PIL import Image,ImageDraw,ImageFont
#
# img=Image.open('./static/upload/22222.jpg')
# 
# #打印图片的尺寸
# print(img.size)
# #生成画笔对象
# draw=ImageDraw.Draw(img)
# #修改图片
# draw.text((0,0),'哈哈',fill=(256,256,256,100))
# #查看图片
# # img.show()
#
# #存储图片
#
# img.save('./static/upload/22222.jpg')

# image=Image.open("./static/upload/22222.jpg")
# text='测试图片'
# font=ImageFont.truetype('C:\\Windows\\Fonts\\Tahoma.ttf',100)
# layer=image.convert('RGB')
# text_overlay=Image.new('RGB',layer.size,(255,255,255,0))
# image_draw=ImageDraw.Draw(text_overlay)
# text_x,text_y=image_draw.textsize(text,font=font)
# text_xy=(layer.size[0]-text_x,layer.size[1]-text_y)
# image_draw.text(text_xy,text,font=font,fill=(255,255,255,50))
# after=Image.alpha_composite(layer,text_overlay)
# after.save('./static/upload/5555.jpg')

# #打开图片
# im = Image.open("./static/upload/2000.png").convert('RGBA')
# #新建一个空白图片,尺寸与打开图片一样
# txt=Image.new('RGBA', im.size, (0,0,0,0))
# #设置字体
# fnt=ImageFont.truetype("c:/Windows/Fonts/Tahoma.ttf", 40)
# #操作新建的空白图片>>将新建的图片添入画板
# d=ImageDraw.Draw(txt)
# #在新建的图片上添加字体
# d.text((txt.size[0]-115,txt.size[1]-80), "i am iron man",font=fnt, fill=(100,100,100,100))
# #合并两个图片
# out=Image.alpha_composite(im, txt)
# # out.show()
# out.save("./static/upload/22222.png")
#

from PIL import Image, ImageDraw, ImageFont

img = Image.open('./static/upload/huayu.jpg' )
# 生成画笔
draw = ImageDraw.Draw(img)
# 定义字体
my_font = ImageFont.truetype(font='c:\\Windows\\Fonts\\msyh.ttc', size=40)
# 打水印
draw.text((20, 20), '奇奇', fill=(76, 234, 124, 180), font=my_font)
# 查看图片
# img.show()
# 有水印图片的名称

# 存储图片
img.save('./static/upload/huayu.jpg')
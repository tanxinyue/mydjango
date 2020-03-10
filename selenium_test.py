import urllib

from selenium import webdriver
import time
import requests
import json
import base64
browser=webdriver.Chrome('./chromedriver.exe')


browser.get('http://localhost:8080/register')


time.sleep(3)

image=browser.find_element_by_xpath('//*[@id="app"]/div/section/div/teble/tr[4]/td[2]/img')
image.screenshot('yzm.png')



# 请求百度接口
res=requests.get('https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=9iAHiBOGO2cI2KwZGNVjmB5o&client_secret=LzNslIvnf9sUfnekUMxTAw6GPTbh818R')
res=json.loads(str(res.text))
print(res)
token=res['access_token']
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token"+token

print(token)

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open('./yzm.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = token
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
    print(type(response.json()))
    word=response.json()['words_result'][0]['words']
    browser.find_element_by_xpath('//*[@id="app"]/div/section/div/teble/tr[3]/td[2]/input').send_keys(word)














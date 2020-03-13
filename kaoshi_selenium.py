
from selenium import webdriver
import time


from selenium.webdriver import ActionChains
browser=webdriver.Chrome('./chromedriver.exe')
browser.get('http://127.0.0.1:8080/ks_log')
time.sleep(3)
browser.find_element_by_xpath('//*[@id="app"]/div/section/div/table/tr[1]/td[2]/input').send_keys('刘德华')
time.sleep(5)
browser.find_element_by_xpath('//*[@id="app"]/div/section/div/table/tr[2]/td[2]/input').send_keys('123')
time.sleep(3)

#定义拖动对象
slipt=browser.find_element_by_xpath('//*[@id="app"]/div/section/div/table/tr[3]/td[2]/div/div[3]')
print(slipt)
#获取按钮长度
splipt_len=slipt.size.get('width')
print(splipt_len)
box=browser.find_element_by_xpath('//*[@id="app"]/div/section/div/table/tr[3]/td[2]/div/div[2]')
box_len=box.size.get('width')

all_len=box_len-splipt_len
all_len=int(all_len)
cation=ActionChains(browser)
cation.click_and_hold(slipt).perform()
#释放动作
cation.reset_actions()
#拖动距离
cation.move_by_offset(all_len,0).perform()
time.sleep(5)
#点击登录按钮
browser.find_element_by_xpath('//*[@id="app"]/div/section/div/table/tr[4]/td[2]/button').click()


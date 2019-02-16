#coding:utf-8
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def write(item):
    with open(r"F:\DOCUMENT\SELENIUM\第六章\jrtt.csv","a") as f:
        writer=csv.writer(f)
        try:
            writer.writerow(item)
        except:
            print("error")

def getinfo():
        id_=dr.find_element_by_xpath('//*/div[@class="article-sub"]/span[1]')
        time_=dr.find_element_by_xpath('//*/div[@class="article-sub"]/span[2]')
        title_=dr.find_element_by_xpath('//*/h1[@class="article-title"]')
        text_=dr.find_element_by_xpath('//*/div[@class="article-content"]')
        item=[id_.text,time_.text,title_.text,text_.text]
        return item

url="https://www.toutiao.com/search/?keyword=selenium"
dr=webdriver.Chrome()
dr.implicitly_wait(2)
dr.get(url)

#给页面留下足够的时间加载
time.sleep(1)

#下拉页面，刷新出足够的条数
for i in range(10000): #这里循环次数尽量大，保证加载到底
        #相当于一直按着DOWN键
        ActionChains(dr).key_down(Keys.DOWN).key_up(Keys.DOWN).perform()
        print(f'下拉已完成{i}次')

#再次留下时间加载，因为无法确定最后刷新到了哪一个，所以不用显式等待
time.sleep(1)
url_=dr.find_elements_by_css_selector('.title')
print(url_)

#链接列表
url_list=[]
for i in url_:
    url_list.append(i.get_attribute('href'))
print(url_list)

#考虑到部分可能会出错，我们使用try，except来接收报错
for i in url_list:
    try:

        dr.get(i)
        time.sleep(0.5)
        write(getinfo())
        dr.get(url)
        print('已完成写入')
    except:
        print("error")
print('all_done')
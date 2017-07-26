#coding=utf-8
import re
import time
import random
from urllib import quote
import os
import urllib
class get_mx_image:
    def __init__(self):
        mx_name = raw_input("请输入你想要看的明星名字: ")
        mx_dir=mx_name
        mx_new_name=quote(mx_name)
        x = raw_input("请输入你想看的页数: ")
        self.name = mx_new_name
        self.page = x
        self.mx_name = mx_name
        self.mkpath ="./%s" % (str(mx_dir))
        if os.path.isdir(self.mkpath):
            pass
        else:
            os.mkdir(self.mkpath)
        pass

    def get_url(self):
        r=random.randint(100, 999)
        date = str(int(time.time()))+str(r)
        for y in xrange(1,int(self.page)+1):
            p = 30 * int(self.page)
            url="https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={0}=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={1}=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={2}&rn=30&gsm=1e&{3}=".format(self.name,self.name,p,date)
            html=self.getHtml(url)
            mx_f_dir="./%s/%d" % (str(self.mx_name),int(y))
            self.make_dir(mx_f_dir)
            self.getImg(html,y)

    def make_dir(self,new_path):
        if os.path.isdir(new_path):
            pass
        else:
            os.mkdir(new_path)
        pass
    def getHtml(self,url):
        page = urllib.urlopen(url)
        html = page.read()
        return html

    def getImg(self,html,y):
        reg = r'thumbURL":"(.+?\.jpg)",'
        imgre = re.compile(reg)
        imglist = re.findall(imgre,html)
        num = 0
        for imgurl in imglist:
            urllib.urlretrieve(imgurl,'./%s/%d/%s.jpg' % (str(self.mx_name),int(y),num))
            num+=1
        print 'ok'
get_mx_image=get_mx_image()
get_mx_image.get_url()
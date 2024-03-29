# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
import ssl


# 获取维基百科词条信息
ssl._create_default_https_context = ssl._create_unverified_context  # 全局取消证书验证

# 请求URL，并把结果用utf-8编码
req = urlopen("https://en.wikipedia.org/wiki/Main_page", timeout=10).read().decode("utf-8")

# 使用beautifulsoup去解析
soup = bs(req, "html.parser")

# 获取所有href属性以“/wiki/Special”开头的a标签
urllist = soup.findAll("a", href=re.compile("^/wiki/Special"))

for url in urllist:
    # 去除以.jpg或.JPG结尾的链接
    if not re.search("\.(jpg|JPG)$", url["href"]):
        # get_text()输出标签下的所有内容，包括子标签的内容；
        # string只输出一个内容，若该标签有子标签则输出“none
        print(url.get_text() + "----->" + url["href"])

import MySQLdb
import datetime
'''连接数据库'''
db = MySQLdb.connect(host = 'localhost',#本地数据库
user = 'root', #用户名
passwd = 'hhyytt2003', #数据库密码
db = 'test', #数据库名
charset = 'utf8')  #数据库编码
'''待插入的数据'''
Url = "http://www.baidu.com"
Time = datetime.datetime.now() #系统当前时刻

'''插入数据'''

'''关闭连接'''
db.close()
import requests
from bs4 import BeautifulSoup
import selenium

# 爬虫三大模块 url管理器 网页下载器 网页解析器
"""
发送request请求(get/post) 提交表单用post
url：要下载的目标的网址
data 用于post方法时提交数据
headers 设置user-agent，refer等请求头
timeout 超时时间，单位s


import requests
url = 'http://httpcn.com'
r = requests.get(url)
r.status_code
200
r.headers
{'Content-Type': 'text/html', 'Content-Encoding': 'gzip', 'Vary': 'Accept-Encoding', 'Server': 'Microsoft-IIS/10.0', 'X-Powered-By': 'ASP.NET', 'Date': 'Thu, 21 Mar 2024 02:33:21 GMT', 'Content-Length': '42501'}
r.encoding = 'utf-8'
r.text

r.cookies
<RequestsCookieJar[]>

"""
print('ok')
url = 'http://crazyant.net'

r = requests.get(url)
u = r.status_code
print(u)

#-*-coding:utf8-*-
# 爬取教务处上课程表

import re
import requests
import sys

# get source code of a webset
url = 'http://10.5.2.80/(qx4h3fzj0nv32s45xlxy5szg)/default2.aspx'
headers = {'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
username=raw_input('input your school id here')
password=raw_input('input your password here')
data={
    'TextBox1':username,
    'TextBox2':password
}
html=requests.post(url,data=data).text
# html.encoding = 'utf-8'
print html

# data={
#     'entities_only':'true',
#     'page':'1'
# }
# html_post = requests.post(url,data=data)
# title = re.findall('"card-title">(.*?)</div>',html_post.text,re.S)
# for each in title:
#     print each
# find the content by re
# title = re.findall('src=(.*?)>',html.text,re.S)
# for each in title:
#     print each


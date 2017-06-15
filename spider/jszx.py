#-*-coding:utf8-*-
# 用于爬取急速之星电影名称

import requests
import re
import chardet

# 输入密码，用户名等
password ='xxxxx'
username ='xxxxx'
url = 'http://bitpt.cn/takelogin.php'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
}
data ={
    'username':username,
    'questionid':'0',
    'password':password
}

# 内容爬取
html = requests.post(url, data=data)
print html.content
# print chardet.detect(html)
# list = re.findall('target=_blank><b>(.*?)</b></A>', html.text)
# print list[0]
# for each in list:
#     print each
# for each in list:
#     print each
    # context = unicode.encode(each,'utf-8')
    # print each.decode(encoding='UTF-8',errors='strict')
# -*-coding:utf8-*-
# 嗅事百科

import request
import re
import chardet

# 输入密码，用户名等

url = 'https://www.qiushibaike.com/hot/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
}

# 内容爬取
html = requests.get(url)
# print(html.content.decode('utf-8'))
# print chardet.detect(html)
list = re.findall('<span>(.*?)</span>', html.text)
for i in range(len(list)-10):
    if '<' in list[i] or len(list[i])<50:
        continue
    print(list[i])

# for each in list:
#     print each
# for each in list:
#     print each
# context = unicode.encode(each,'utf-8')
# print each.decode(encoding='UTF-8',errors='strict')

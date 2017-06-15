#-*-coding:utf-8-*-
# 课程中给出的爬取豆瓣电影的样例

import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# Python中 import 只执行一次，后续的 import 仅仅在 sys.modules 中查找是否存在对应的模块对象，而对于源文件进行修改后想要立即重新导入该文件而不想整体重新执行程序时， reload 就在该处派上用途了。在实际中，测试代码修改结果，或者对于不能停止的服务需要动态改变运行行为 reload 是非常有用的。
# reload 的执行流程如下所示：
# 1）在 sys.modules 中查找到对应模块名的模块对象；
# 2）针对该模块名的 执行文件 属性，找到对应文件并重新编译该文件执行；
# 3）将代码执行中产生的对象依次更新到原模块对象的属性中；
class spider(object):
    def __init__(self):
        print u'开始内容爬取'

#获取源码
    def getsource(self,url):
        html=requests.get(url)
        return html.text

    # 翻页
    def changepage(self,url,total_page):
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group = []
        for i in range(now_page,total_page+1):
            link = re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)#产生新的链接
            page_group.append(link)
        return page_group

    #获取课程数
    def geteveryclass(self,source):
        everyclass=re.findall('(<li deg="".*?</li>)',source,re.S)
        return everyclass
    #记录课程信息
    def getinfo(self,eachclass):
        info={}
        info['title'] = re.search('target="_blank">(.*?)</a>', eachclass, re.S).group(1)
        info['content'] = re.search('</h2><p>(.*?)</p>', eachclass, re.S).group(1)
        timeandlevel = re.findall('<em>(.*?)</em>', eachclass, re.S)
        info['classtime'] = timeandlevel[0]
        info['classlevel'] = timeandlevel[1]
        info['learnnum'] = re.search('"learn-number">(.*?)</em>', eachclass, re.S).group(1)
        return info
    #保存信息
    def saveinfo(self,classinfo):
        f = open('info.txt', 'a')
        for each in classinfo:
            f.writelines('title:' + each['title'] + '\n')
            f.writelines('content:' + each['content'] + '\n')
            f.writelines('classtime:' + each['classtime'] + '\n')
            f.writelines('classlevel:' + each['classlevel'] + '\n')
            f.writelines('learnnum:' + each['learnnum'] + '\n\n')
        f.close()
if __name__=='__main__':
    classinfo=[]
    url='http://www.jikexueyuan.com/course/?pageNum=1'
    jikespider=spider()
    all_links=jikespider.changepage(url,20)
    for link in all_links:
        print u'正在处理页面：'+link
        html=jikespider.getsource(link)
        everyclass=jikespider.geteveryclass(html)
        for each in everyclass:
            info=jikespider.getinfo(each)
            classinfo.append(info)
        jikespider.saveinfo(classinfo)



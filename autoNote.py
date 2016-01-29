#!/usr/bin/evn bash
#encoding=utf-8

# 为了自己写日记方便一点，自动的为我轻松的复制与命名当天的任务！
# 要实现的功能：
# 1. 运行角本可以自动的复制模版当天任务，给其命名一个正确的时间格式代码！ 自动的创建文件夹，按年月分类，一个年的分成几个月，这个有点难吧
# 2. 是运用shell 脚本实现自动的日志的上传与更新！
# 3. 还没有想好，不知道现在github 可以用了没有

import time
import os
import re
PATH="/home/linzi/note/log/"

#取得模板
f=open("/home/linzi/note/log/template/logTemp.md")
text=f.read()

f.close()
# 取得当前时间的函数
def gettimes():
    timestr=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    return timestr
def getyear():
    year=time.strftime('%Y',time.localtime(time.time()))
    return year
def getmouth():
    mouth=time.strftime('%m',time.localtime(time.time()))
    return mouth
    
#获取昨天日记的路径
def getyetPath():
    year=time.strftime('%Y',time.localtime(time.time()-60*60*24))
    mouth=time.strftime('%m',time.localtime(time.time()-60*60*24))
    timestr=time.strftime('%Y-%m-%d',time.localtime(time.time()-60*60*24))
    path=PATH+year+'/'+mouth+'/'+timestr+'.md'
    return path
# 对目录是否要创建的定
def mkdir():
    path=PATH+getyear()+'/'+getmouth()
    print path
    if os.path.exists(path):
        print "目录存在"
    else:
        print "目录不存在,正在创建目录。。。。。。。"
        os.makedirs(path)
mkdir()

# 取得昨日的计划的函数
def getyesplan():
    f=open(getyetPath(),'r')
    yesplan=f.read()
    f.close()
    plan=re.findall("start--([\s\S]*?)--end",yesplan)
    str=''
    for each in plan:
        str+=each
    return str
    
#替换计划任务为今日任务
def replaceplan():
    result, number=re.subn('--begin--([\s\S]*?)--end--',getyesplan(),text)
    results,number=re.subn('==(.*?)==',gettimes(),result)
    print results
    return results
#写入日志
def writelog():
    path=PATH+getyear()+'/'+getmouth()+'/'+gettimes()+'.md'
    print(path)
    f=open(path,"w")
    f.write(replaceplan())
    f.close()

print getyesplan()
# 替换明日计划
def isexists():
    path=PATH+getyear()+'/'+getmouth()+'/'+gettimes()+'.md'
    if os.path.exists(path):
        return "今天的日志已经有了，请去"+path+"查看当天日志"
    else:
        writelog()
        return "今日日志成功的创建了，请到"+path+"查看当天日志"
print isexists()

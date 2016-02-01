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
## 对获取时间的代码重构
def getTimes(timeX):
    timestr=time.strftime('%Y-%m-%d',time.localtime(time.time()+60*60*24*timeX))
    year=time.strftime('%Y',time.localtime(time.time()+60*60*24*timeX))
    mouth=time.strftime('%m',time.localtime(time.time()+60*60*24*timeX))
    return year,mouth,timestr

# 对获取路径的代码重构

def getPath(pathX):
    year,mouth,timestr=getTimes(pathX)
    path=PATH+year+'/'+mouth+'/'+timestr+'.md'
    mouthPath=PATH+year+'/'+mouth
    return path,mouthPath


# 对目录是否要创建的定
def mkdir():
    filepath,path=getPath(0)
    print path
    if os.path.exists(path):
        print "目录存在"
    else:
        print "目录不存在,正在创建目录。。。。。。。"
        os.makedirs(path)
mkdir()

#取得昨天没成完的任务
def getyesPath():
    pathX=-1
    path,mouthPath=getPath(pathX)
    while(not(os.path.exists(path))):
        pathX-=1
        print pathX
        path,mouthPath=getPath(pathX)
    print path
    return path

def getyesnoplan():
    path=getyesPath()
    f=open(path,'r')
    yesnoplan=f.read()
    f.close()
    noplans=re.findall("--begin--([\s\S]*?)--end--",yesnoplan)
    strs=''
    for each in noplans:
        strs+=each
    str=''
    noplan=re.findall("(....\+\ \[\]\ .*)",strs)
    for each in noplan:
        str+=(each+'\n')
    print str
    return str
# 取得昨日的计划的函数
def getyesplan():
    f=open(getyesPath(),'r')
    yesplan=f.read()
    f.close()
    plan=re.findall("--start--([\s\S]*?)--ends--",yesplan)
    str=''
    for each in plan:
        str+=each
    return str

#替换计划任务为今日任务
def replaceplan():
    year,mouth,timestr=getTimes(0)
    todayplan='--begin--\n'+'''#### 昨日未完成任务'''
    todayplan+='\n'+getyesnoplan()
    todayplan+='\n'+'''#### 今日任务'''+getyesplan()+'\n\t--end--\n'
    result, number=re.subn('--begin--([\s\S]*?)--end--',todayplan,text)
    results,number=re.subn('==(.*?)==',timestr,result)
    return results
#写入日志
def writelog():
    path,mouthPath=getPath(0)
    f=open(path,"w")
    f.write(replaceplan())
    f.close()

print getyesplan()
# 替换明日计划
def isexists():
    path,mouthPath=getPath(0)
    if os.path.exists(path):
        return "今天的日志已经有了，请去"+path+"查看当天日志"
    else:
        writelog()
        return "今日日志成功的创建了，请到"+path+"查看当天日志"


# 在这里加一个昨日任务没有完成的，自动的添加到明日任务中

print isexists()

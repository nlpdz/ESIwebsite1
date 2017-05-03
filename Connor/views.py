# -*- coding:utf-8 -*-
from django.shortcuts import render
from Connor import models
from django.http import HttpResponse
import json
# Create your views here.

# 登陆界面控制器
def login(request):
    return render(request, "login.html")
# 主界面框架控制器
def index(request):
    if request.method == "POST":
        username = request.POST.get("_ctl0:txtusername", None)
        password = request.POST.get("_ctl0:txtpassword", None)
    if not models.UserInfo.objects.filter(user="nlp", pwd="nlp503"):
        models.UserInfo.objects.create(user="nlp", pwd="nlp503")
    info = models.UserInfo.objects.filter(user=username, pwd=password)
    if info:
        return render(request, "index.html")
    else:
        return render(request,"login.html",{"message":"用户不存在或密码错误"})
# 主界面顶部控制器
def topFrame(request):
    return render(request,"topFrame.html")
# 主界面顶部第二栏控制器
def colFrame(request):
    import time
    data = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return render(request, "colFrame.html",{"data" : data})
# 主界面左侧菜单控制器
def MenuFrame(request):
    return render(request,"MenuFrame.html")
# 主界面左侧展开收起控制器
def pushRLFrame(request):
    return render(request,"pushRLFrame.html")
# 主界面默认内容控制器
def PageFrame(request):
    import time
    data = time.strftime('%Y %m %d', time.localtime(time.time()))
    y, m, d = data[:4], data[5:7], data[8:]
    mist = ["02", "04", "06", "08", "10", "12"]
    dist = ["31", "31", "28", "30", "30", "31"]
    m1 = int(m)
    y1 = int(y)
    mstart = "1"
    daystart = "1"
    yend = y
    if m1 >= 1 and m1 < 3:
        # 16.10.31
        mend = mist[4]
        ystart = y1 - 11
        yend = str(y1 - 1)
        dayend = dist[0]
    elif m1 >= 3 and m1 < 5:
        # 16.12.31
        mend = mist[5]
        ystart = y1 - 11
        yend = str(y1 - 1)
        dayend = dist[1]
    elif m1 >= 5 and m1 < 7:
        # 17.02.28
        mend = mist[0]
        ystart = y1 - 10
        # 运算符优先级 not > and > or
        if y1 % 100 != 0 and y1 % 4 == 0 or y1 % 400 == 0:
            dayend = "29"
        else:
            dayend = dist[2]
    elif m1 >= 7 and m1 < 9:
        mend = mist[1]
        ystart = y1 - 10
        dayend = dist[3]
    elif m1 >= 9 and m1 < 11:
        mend = mist[2]
        ystart = y1 - 10
        dayend = dist[4]
    else:
        mend = mist[3]
        ystart = y1 - 10
        dayend = dist[5]
    startdata = str(ystart) + "-01-01"
    enddata = yend + "-" + mend + "-" + dayend
    if request.method == "POST":
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        btn = "暂停"
        status = 1
        result = "Error!"
        return HttpResponse(json.dumps({
            "status": status,
            "result": result,
            "btn": btn
        }))
    return render(request,"PageFrame.html",{"startdata" : startdata, "enddata" : enddata})
#论文统计控制器
def Page_lwtj(request):
    return render(request,"Page_lwtj.html")
#论文统计控制器
def spiderSen(request):
    return render(request,"PageFrame.html")
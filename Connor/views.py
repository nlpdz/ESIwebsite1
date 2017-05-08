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
    else:
        return render(request, "login.html", {"message": "走正门"})
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
    import tools
    startdata, enddata = tools.daterange()
    if request.method == "POST":
        import sys
        sys.path.append("..")
        from spider.crawl_list import ESIspider
        from Connor.models import EsiDissertation
        es = ESIspider()
        title, context, author, publication = es.get_SCIurl()
        EsiDissertation.objects.create(title=title, author=author, context=context, publication=publication)
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
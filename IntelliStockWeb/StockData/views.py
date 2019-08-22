from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import STK_TrigSent
from .models import STK_Code
from django.utils import timezone
import datetime
from StockData import services

def index(request):
    return render(request, 'StockData/index.html')

def analyzethis(request):
    if request.method == 'POST':
        print("dsfds")
        retTxt = services.extracttextfromhtml(request.POST['urltoextract'])
        matched_content = services.matchText(retTxt["CleanContent"],request.POST['matchtxt'])
        print("matched_content",matched_content)
        return render(request, 'StockData/AnalyzeThis.html',{'content_todisp': retTxt["CleanContent"], 'matched_content': matched_content})
    elif request.method == 'GET':
        print("Is this the issue?")
        return render(request, 'StockData/AnalyzeThis.html')
    return

def dispTrigSent(request,strMsg=""):
    stkcds  = STK_Code.objects.filter()
    if strMsg == "":
        return render(request, 'StockData/Trigger.html', {'stkcds':stkcds})
    else:
        print("in here?",strMsg)
        return render(request, 'StockData/Trigger.html', {'stkcds':stkcds,'error_message': "Triggered smart analysis for - " + strMsg + " Wait for it!!! "})

def setTrigSent(request):
    try:
        if request.method == 'POST':
            retMsg = request.POST['stkId']
            stk_code_obj = STK_Code.objects.filter(stk_code=retMsg)[0]
            objtrigsent = STK_TrigSent(stk_code=stk_code_obj,stk_TrigStat=1,stk_TrigDtTm=datetime.datetime.now())
            objtrigsent.save()
            return dispTrigSent (request,retMsg)
        elif request.method == 'GET':
            print("Is this the issue?")
            return dispTrigSent (request)
    except Exception as e:
        print(e)
        return render(request, 'StockData/Trigger.html',{'error_message': "FUCKED!"})

def getTrigStks (request):
    try:
        stkcd = STK_TrigSent.objects.filter(stk_TrigStat=1)
        return render(request, 'StockData/DispTrigs.html', {'stkTriggers':stkcd})
    except Exception as e:
        print (e)
        return render(request, 'StockData/Trigger.html',{'error_message': "FUCKED!"})

def delTrigStks (request):
    try:
        if request.method == 'POST':
            stkTrigId = request.POST['stkTrigId']
            stkCd = request.POST['stkCd']
            objTrigStk = STK_TrigSent.objects.get(id=stkTrigId)
            objTrigStk.delete()
            return getTrigStks (request)
        elif request.method == 'GET':
            return getTrigStks (request)
    except Exception as e:
        print (e)
        return render(request, 'StockData/Trigger.html',{'error_message': "FUCKED!"})

def extractText(request):
    try:
        print("Lets extract")
        pass
    except Exception as e:
        raise render(request, 'StockData/Trigger.html',{'error_message': "FUCKED!"})

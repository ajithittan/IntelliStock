from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import STK_TrigSent
from .models import STK_Code
from django.utils import timezone
import datetime

def index(request):
    return render(request, 'StockData/index.html')

def dispTrigSent(request):
    stkcds  = STK_Code.objects.filter()
    return render(request, 'StockData/Trigger.html', {'stkcds':stkcds})

def setTrigSent(request):
    try:
        if request.method == 'POST':
            retMsg = request.POST['stkId']
            stk_code_obj = STK_Code.objects.filter(stk_code=retMsg)[0]
            objtrigsent = STK_TrigSent(stk_code=stk_code_obj,stk_TrigStat=1,stk_TrigDtTm=datetime.datetime.now())
            objtrigsent.save()
            return render(request, 'StockData/Trigger.html',{'error_message': "Triggered smart analysis for - " + retMsg + " Wait for it!!! "})
        elif request.method == 'GET':
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
            print("Am I here?")
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

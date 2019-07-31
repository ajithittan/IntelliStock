from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import STK_TrigSent
from .models import STK_Code

import datetime

def index(request):
    return render(request, 'StockData/index.html')

def dispTrigSent(request):
    return render(request, 'StockData/Trigger.html')

def setTrigSent(request):
    try:
        retMsg = request.POST['stkId']
        stk_code_obj = STK_Code.objects.filter(stk_code=retMsg)[0]
        print("stk_code_obj",stk_code_obj)
        objtrigsent = STK_TrigSent(stk_code=stk_code_obj,stk_TrigStat=1,stk_TrigDtTm=datetime.datetime.now())
        #print(objtrigsent)
        objtrigsent.save()
        return render(request, 'StockData/Trigger.html',{'error_message': "Triggered smart analysis for - " + retMsg + " Wait for it!!! "})
    except Exception as e:
        print(e)
        return render(request, 'StockData/Trigger.html',{'error_message': "FUCKED!"})

def getTrigStks (request):
    try:
        print("Am I here?")
        render(request, 'StockData/DispTrigs.html')
    except Exception as e:
        print(e)
        return render(request, 'StockData/Trigger.html',{'error_message': "FUCKED!"})

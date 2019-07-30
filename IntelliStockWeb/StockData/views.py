from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import STK_TrigSent
import datetime

def index(request):
    return render(request, 'StockData/index.html')

def dispTrigSent(request):
    return render(request, 'StockData/Trigger.html')

def setTrigSent(request):
    try:
        retMsg = request.POST['stkId']
        objtrigsent = STK_TrigSent(stk_code=retMsg,stk_TrigStat=1,stk_TrigDtTm=datetime.datetime.now())
        objtrigsent.save()
        return render(request, 'StockData/Trigger.html',{'error_message': retMsg})
    except Exception as e:
        print(e)
        return render(request, 'StockData/Trigger.html',{'error_message': "FUCKED!"})

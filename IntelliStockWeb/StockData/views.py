from django.shortcuts import render
from django.http import HttpResponse
from .models import STK_TrigSent

def index(request):
    return render(request, 'StockData/index.html')

def dispTrigSent(request):
    return render(request, 'StockData/Trigger.html')

def setTrigSent(request):
    return render(request, 'StockData/Trigger.html')

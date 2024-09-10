# example/views.py
from datetime import datetime
from django.http import JsonResponse
from .data import *
from django.http import HttpResponse
from .data import *

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def candlestick(request):
    return JsonResponse(data)

def linechart(request):
    return JsonResponse(data1)

def barchart(request):

    return JsonResponse(data2)

def piechart(request):
    
   return JsonResponse(data3)

# example/views.py
from datetime import datetime
from django.http import JsonResponse
from .data import *
from django.http import HttpResponse
from .data import *
from django.shortcuts import render


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

def candlestick(request):
    return JsonResponse(data)

def linechart(request):
    return JsonResponse(data1)

def barchart(request):

    return JsonResponse(data2)

def piechart(request):
    
   return JsonResponse(data3)

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
        <head>
        <body>
            <h1>Welcome to Habib's Chart Data API!</h1>
            <p>Feel free to use this api for free chart data</p>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

def candlestick(request):
    response = JsonResponse(data)
    return response


def linechart(request):
    return JsonResponse(data1)

def barchart(request):

    return JsonResponse(data2)

def piechart(request):
    
   return JsonResponse(data3)

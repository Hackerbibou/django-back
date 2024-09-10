# example/urls.py
from . import views
from django.urls import path, include
from example.views import index
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path("api/candlestick-data/", views.candlestick, name='candlestick'),
    path("api/line-chart-data/", views.linechart, name='linechart'),
    path("api/bar-chart-data/", views.barchart, name='barchart'),
    path("api/pie-chart-data/", views.piechart, name='piechart'),
]



# example/urls.py
from django.urls import path
from . import views

from example.views import index


urlpatterns = [
    path('', index),
    path("api/candlestick-data/", views.candlestick, name='candlestick'),
    path("api/line-chart-data/", views.linechart, name='linechart'),
    path("api/bar-chart-data/", views.barchart, name='barchart'),
    path("api/pie-chart-data/", views.piechart, name='piechart'),
]
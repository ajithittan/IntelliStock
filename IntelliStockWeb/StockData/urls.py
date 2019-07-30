from django.urls import path

from . import views

app_name = 'StockData'
urlpatterns = [
    path('', views.index, name='index'),
    path('Trigger', views.dispTrigSent, name='Trigger'),
]

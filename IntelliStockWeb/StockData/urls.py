from django.urls import path

from . import views

app_name = 'StockData'
urlpatterns = [
    path('', views.index, name='index'),
    path('Trigger', views.dispTrigSent, name='Trigger'),
    path('setTrigSent', views.setTrigSent, name='Trigger'),
    path('getTrigStks', views.getTrigStks, name='GetTrigger'),
    path('delTrigStks', views.delTrigStks, name='GetTrigger'),
    path('AnalyzeThis', views.analyzethis, name='AnalyzeThis'),
]

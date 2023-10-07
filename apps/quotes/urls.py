from django.contrib import admin
from django.urls import path
from .views import QuoteList,csv_generate, Home, json_generate,LogList,Log_generate, TagList,TagView,UpdateDataBase

urlpatterns = [
    path("quoteList/", QuoteList.as_view(), name="quoteList"),
    path("", Home.as_view(), name="home"),
    path('csv_generate/', csv_generate.as_view(), name='csv_generate'),
    path('json_generate/', json_generate.as_view(), name='json_generate'),
    path('logs/', LogList.as_view(), name="logs"),
    path('log_generate/', Log_generate.as_view(), name='log_generate'),
    path('tagList/', TagList.as_view(), name='tagList'),
    path('tag/', TagView.as_view(), name='tagView'),
    path('updateDataBase/', UpdateDataBase.as_view(), name='updateDataBase'),
    
    

    
]
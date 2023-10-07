from django.contrib import admin
from django.urls import path
from .views import *

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
    path('json_generate_db/', json_generate_db.as_view(), name='json_generate_db'),
    path('csv_generate_db/', csv_generateDB.as_view(), name='csv_generate_db'),
    path('quoteListDB/',QuoteListDB.as_view(), name='quoteListDB'),
    path('tagViewDB/', TagViewDB.as_view(), name='tagViewDB'),
    path('tagListDB/', TagListDB.as_view(), name='tagListDB'),
    

    
]
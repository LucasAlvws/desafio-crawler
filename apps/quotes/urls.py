from django.contrib import admin
from django.urls import path
from .views import QuoteList,csv_generate, Home, json_generate

urlpatterns = [
    path("quoteList/", QuoteList.as_view(), name="quoteList"),
    path("", Home.as_view(), name="home"),
    path('csv_generate/', csv_generate.as_view(), name='csv_generate'),
    path('json_generate/', json_generate.as_view(), name='json_generate' )

    
]
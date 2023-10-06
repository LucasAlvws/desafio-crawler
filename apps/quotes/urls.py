from django.contrib import admin
from django.urls import path
from .views import QuoteList,csv_generate, Home

urlpatterns = [
    path("quoteList/", QuoteList.as_view(), name="quoteList"),
    path("", Home.as_view(), name="home"),
    path('csv_generate/', csv_generate, name='csv_generate'),
]
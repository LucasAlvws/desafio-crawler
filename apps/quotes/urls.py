from django.contrib import admin
from django.urls import path
from .views import QuoteList,download_csv,gerar_relatorio

urlpatterns = [
    path("quotes/", QuoteList.as_view(), name="quotes"),
    path('download_csv/', download_csv, name='download_csv'),
    path('gerar_relatorio/', gerar_relatorio, name='gerar_relatorio'),
]
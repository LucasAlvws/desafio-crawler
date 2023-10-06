from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView
from .conections2site import all_quote_list
import csv

class QuoteList(TemplateView):
    template_name = "quotes/quoteList.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quotes'] = all_quote_list()
        return context

class Home(TemplateView):
    template_name = "quotes/home.html"
    
def csv_generate(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename=quotes.csv'
    writer = csv.writer(response, delimiter =';',quotechar =';')
    writer.writerow(['Quote', 'Author', 'Tags', 'Link'])
    quotes = all_quote_list()
    for q in quotes:   
        writer.writerow([q["Quotes"].replace(";", ":").replace("“", '"').replace("”", '"'), q["Author"], q["Tags"], q["Link"]]) 
    return response

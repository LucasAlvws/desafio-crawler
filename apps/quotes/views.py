from django.http import HttpResponse
from django.views.generic import TemplateView
from .conections2site import all_quote_list
import csv
import json
from django.urls import reverse
from django.views import View


class QuoteList(TemplateView):
    template_name = "quotes/quoteList.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quotes'] = all_quote_list("quoteListMenu")
        return context

class Home(TemplateView):
    template_name = "quotes/home.html"
    

class csv_generate(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = f'attachment; filename=quotes.csv'
        writer = csv.writer(response, delimiter =';',quotechar =';')
        writer.writerow(['Quote', 'Author', 'Tags', 'Link'])
        quotes = all_quote_list("downloadCSVQuoteList")
        for q in quotes:
            writer.writerow([q["Quotes"], q["Author"], q["Tags"], q["Link"]]) 
        return response

class json_generate(View):
    def get(self, request, *args, **kwargs):
        quotes_list = all_quote_list("downloadJSONQuoteList")
        quotes_json = json.dumps(quotes_list, indent=4)
        response = HttpResponse(quotes_json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=quotes.json'
        redirect_url = reverse('quoteList')
        response['Location'] = redirect_url
        return response
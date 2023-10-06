from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .conections2site import all_quote_list, tag_quote_list
import csv
import json
from django.urls import reverse
from django.views import View
from .models import Log


class QuoteList(TemplateView):
    template_name = "quotes/quoteList.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quotes = all_quote_list("quoteListMenu")
        context['quotes'] = quotes
        tags_list = []
        for i in quotes:
            splitTags = i['Tags'].split(",")
            for tag in splitTags:
                if tag not in tags_list:
                    tags_list.append(tag)
        context['tags'] = tags_list
        return context


class Home(TemplateView):
    template_name = "quotes/home.html"
    

class Log_generate(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = f'attachment; filename=logs.csv'
        writer = csv.writer(response, delimiter =';',quotechar =';')
        writer.writerow(['time', 'type', 'location', 'description'])
        logs = Log.objects.all()
        for log in logs:
            writer.writerow([log.time, log.type, log.location, log.description]) 
        return response

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
    def post(self, request, *args, **kwargs):
        pass

class json_generate(View):
    def get(self, request, *args, **kwargs):
        quotes_list = all_quote_list("downloadJSONQuoteList")
        quotes_json = json.dumps(quotes_list, indent=4)
        quotes_json = quotes_json.replace("[", "").replace("]", "")
        response = HttpResponse(quotes_json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=quotes.json'
        redirect_url = reverse('quoteList')
        response['Location'] = redirect_url
        return response

class LogList(ListView):
    template_name = "quotes/logList.html"
    model = Log
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-id')
        return queryset







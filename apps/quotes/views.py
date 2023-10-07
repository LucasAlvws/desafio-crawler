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
        return context


class TagList(TemplateView):
    template_name = "quotes/tagList.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quotes = all_quote_list("tagListMenu")
        tags_list = []
        for i in quotes:
            splitTags = i['Tags'].split(",")
            for tag in splitTags:
                if tag not in tags_list:
                    tags_list.append(str(tag))
        context['tags'] = tags_list
        return context


class TagView(TemplateView):
    template_name = "quotes/quoteList.html"
    def get_context_data(self, **kwargs):
        try:
            tag = self.request.GET.get('tag', None)
        except:
            tag = ""
        context = super().get_context_data(**kwargs)
        quotes = tag_quote_list(f"tagView:{tag}", tag)
        context['quotes'] = quotes
        context['tag'] = tag
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
        Log.objects.create(type=f"GENERATED", location = "Log_generate", description=f"Logs CSV generated")
        return response

class csv_generate(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = f'attachment; filename=quotes.csv'
        writer = csv.writer(response, delimiter =';',quotechar =';')
        writer.writerow(['Quote', 'Author', 'Tags', 'Link'])
        if self.request.GET.get('tag', None) is None:
            quotes = all_quote_list("downloadCSVQuoteList")
        else:
            tag = self.request.GET.get('tag', None)
            quotes = tag_quote_list(f"downloadCSVTag:{tag}", tag)
        for q in quotes:
            writer.writerow([q["Quotes"], q["Author"], q["Tags"], q["Link"]]) 
        Log.objects.create(type=f"GENERATED", location = "csv_generate", description=f"CSV Quotes generated")
        return response

class json_generate(View):
    def get(self, request, *args, **kwargs):
        if self.request.GET.get('tag', None) is None:
            quotes_list = all_quote_list("downloadJSONQuoteList")
        else:
            tag = self.request.GET.get('tag', None)
            quotes_list = tag_quote_list(f"downloadJSONTag:{tag}", tag)
        quotes_json = json.dumps(quotes_list, indent=4)
        quotes_json = quotes_json.replace("[", "").replace("]", "")
        response = HttpResponse(quotes_json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=quotes.json'
        redirect_url = reverse('quoteList')
        response['Location'] = redirect_url
        Log.objects.create(type=f"GENERATED", location = "json_generate", description=f"JSON Quotes generated")
        return response

class LogList(ListView):
    template_name = "quotes/logList.html"
    model = Log
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-id')
        return queryset







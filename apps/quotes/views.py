from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.core.serializers import serialize
from django.urls import reverse
from django.views import View
from django.shortcuts import render
import pandas as pd
import csv
import json
from .models import Log,Quote
from .conections2site import all_quote_list, tag_quote_list




#+++++++BASE+++++++
class Home(TemplateView):
    template_name = "quotes/home.html"   
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "Home", description=f"Error in get method quotes.view.Home: {e}")

class LogList(ListView):
    template_name = "quotes/logList.html"
    model = Log
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-id')
        return queryset
        
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "LogList", description=f"Error in get method quotes.view.LogList: {e}")

class Log_generate(View):
    def get(self, request, *args, **kwargs):
        try:
            response = HttpResponse(content_type='text/csv; charset=utf-8')
            response['Content-Disposition'] = f'attachment; filename=logs.csv'
            writer = csv.writer(response, delimiter =';',quotechar =';')
            writer.writerow(['time', 'type', 'location', 'description'])
            logs = Log.objects.all()
            for log in logs:
                writer.writerow([log.time, log.type, log.location, log.description]) 
            Log.objects.create(type=f"GENERATED", location = "Log_generate", description=f"Logs CSV generated")
            return response
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "Log_generate", description=f"Error in get method quotes.view.Log_generate: {e}")
            messages.error(request, 'ERRO to generate log')
            return HttpResponseRedirect(reverse("home"))
        

#+++++++AO VIVO+++++++
class QuoteList(TemplateView):
    template_name = "quotes/quoteList.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quotes = all_quote_list("quoteListMenu")
        context['quotes'] = quotes
        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "QuoteList", description=f"Error in get method quotes.view.QuoteList: {e}")
                
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
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "TagList", description=f"Error in get method quotes.view.TagList: {e}")
            
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
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "TagView", description=f"Error in get method quotes.view.TagView: {e}")
        
class csv_generate(View):
    def get(self, request, *args, **kwargs):
        try:
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
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "csv_generate", description=f"Error in get method quotes.view.csv_generate: {e}")
            messages.error(request, 'ERRO to generate file')
            return HttpResponseRedirect(reverse("home"))
        
class json_generate(View):
    def get(self, request, *args, **kwargs):
        try:
            if self.request.GET.get('tag', None) is None:
                quotes_list = all_quote_list("downloadJSONQuoteList")
            else:
                tag = self.request.GET.get('tag', None)
                quotes_list = tag_quote_list(f"downloadJSONTag:{tag}", tag)
            quotes_json = json.dumps(quotes_list, indent=4)
            quotes_json = quotes_json
            response = HttpResponse(quotes_json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename=quotes.json'
            redirect_url = reverse('quoteList')
            response['Location'] = redirect_url
            Log.objects.create(type=f"GENERATED", location = "json_generate", description=f"JSON Quotes generated")
            return response
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "json_generate", description=f"Error in get method quotes.view.json_generate: {e}")
            messages.error(request, 'ERRO to generate file')
            return HttpResponseRedirect(reverse("home"))
        

#+++++++BANCO DE DADOS+++++++
class QuoteListDB(TemplateView):
    template_name = "quotes/quoteListDB.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quotes = Quote.objects.all()
        context['quotes'] = quotes
        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "QuoteListDB", description=f"Error in get method quotes.view.QuoteListDB: {e}")

class TagListDB(TemplateView):
    template_name = "quotes/tagListDB.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quotes = Quote.objects.all()
        tags_list = []
        for i in quotes:
            splitTags = i.tags.split(",")
            for tag in splitTags:
                if tag not in tags_list:
                    tags_list.append(str(tag))
        context['tags'] = tags_list
        return context
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "TagListDB", description=f"Error in get method quotes.view.TagListDB: {e}")

class TagViewDB(TemplateView):
    template_name = "quotes/quoteListDB.html"
    def get_context_data(self, **kwargs):
        try:
            tag = self.request.GET.get('tag', None)
        except:
            tag = ""
        context = super().get_context_data(**kwargs)
        quotes = Quote.objects.filter(tags__contains=tag)
        context['quotes'] = quotes
        context['tag'] = tag
        return context
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "TagViewDB", description=f"Error in get method quotes.view.TagViewDB: {e}")

class csv_generate_db(View):
    def get(self, request, *args, **kwargs):
        try:
            response = HttpResponse(content_type='text/csv; charset=utf-8')
            response['Content-Disposition'] = f'attachment; filename=quotes.csv'
            writer = csv.writer(response, delimiter =';',quotechar =';')
            writer.writerow(['Quote', 'Author', 'Tags', 'Link'])
            if self.request.GET.get('tag', None) is None:
                quotes = Quote.objects.all()
            else:
                tag = self.request.GET.get('tag', None)
                quotes = Quote.objects.filter(tags__contains=tag)
            for q in quotes:
                writer.writerow([q.quote, q.author, q.tags, q.link]) 
            Log.objects.create(type=f"GENERATED", location = "csv_generateDB", description=f"CSV Quotes DB generated")
            return response
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "csv_generateDB", description=f"Error in get method quotes.view.csv_generateDB: {e}")
            messages.error(request, 'ERRO to generate file')
            return HttpResponseRedirect(reverse("home"))
        
class json_generate_db(View):
    def get(self, request, *args, **kwargs):
        try:
            if self.request.GET.get('tag', None) is None:
                quotes = Quote.objects.all()
            else:
                tag = self.request.GET.get('tag', None)
                quotes = Quote.objects.filter(tags__contains=tag)
            serialized_quotes = serialize('json', quotes)
            json_data = json.loads(serialized_quotes)
            json_string = json.dumps(json_data, indent=4)
            response = HttpResponse(json_string, content_type='application/json')
            response['Content-Disposition'] = f'attachment; filename="quotes.json"'
            Log.objects.create(type=f"GENERATED", location = "json_generate_db", description=f"JSON Quotes DB generated")
            return response  
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "json_generate_db", description=f"Error in get method quotes.view.json_generate_db: {e}")
            messages.error(request, 'ERRO to generate file')
            return HttpResponseRedirect(reverse("home"))

class UpdateDataBase(View):
    def get(self, request, *args, **kwargs):
        try:
            site_quotes = all_quote_list("UpdateDataBase")
            for s_quote in site_quotes:
                if len(Quote.objects.filter(quote=s_quote['Quotes'])) == 0:
                    Quote.objects.create(quote=s_quote['Quotes'],author=s_quote['Author'],tags=s_quote['Tags'],link=s_quote['Link'])
            Log.objects.create(type=f"UPDATED", location = "UpdateDataBase", description=f"Database updated")
            messages.success(request, 'Database Updated')
            return HttpResponseRedirect(reverse("home"))
        except Exception as e:
            Log.objects.create(type=f"ERROR", location = "UpdateDataBase", description=f"Error in get method quotes.view.UpdateDataBase: {e}")
            messages.error(request, 'ERRO Database Updated')

class Pandas(TemplateView):
    template_name = "quotes/pandas.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quotes = Quote.objects.all().values()
        data = pd.DataFrame(quotes)
        context['data'] = data.to_html()
        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            Log.objects.create(type=f"Pandas", location = "QuoteListDB", description=f"Error in get method quotes.view.Pandas: {e}")           


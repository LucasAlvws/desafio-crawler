from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView
from .conections2site import list_of_dict
import csv

class QuoteList(TemplateView):
    template_name = "quotes/quoteList.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quotes'] = list_of_dict()
        return context


def download_csv(request):
    txt_data = ""
    if "GET" == request.method:
        try:
            txt_data = str(list_of_dict()).replace("}", "\n")
        except Exception as e:
            messages.error(request, 'Erro Geral. Contate a TI. ' + str(e))
        response = HttpResponse(txt_data.replace('"', ''), content_type='application/text')
        response['Content-Disposition'] = 'attachment; filename="quotes.csv"'
        return response

def gerar_relatorio(request):
    # Cria o objeto HttpResponse com o cabeçalho CSV apropriado.
    response = HttpResponse()
    response['Content-Disposition'] = f'attachment; filename=quotes.csv'
    writer = csv.writer(response, delimiter =';',quotechar =';')
    writer.writerow(['Quote', 'Author', 'Tags', 'Link'])
    quotes = list_of_dict()
    for q in quotes:   
        writer.writerow([q["Quotes"].replace(";", ":").replace("“", '"').replace("”", '"'), q["Author"], q["Tags"], q["Link"]]) 
    return response

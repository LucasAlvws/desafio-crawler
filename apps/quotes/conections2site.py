import requests
from bs4 import BeautifulSoup
from .models import Log
'''url='http://quotes.toscrape.com/'
response=requests.get(url)
doc=BeautifulSoup(response.text,'html.parser')
div_tags=doc.find_all('div',class_='quote')'''

def all_quote_list(local):
    try:
        lista_quotes = []
        next_page = True
        link = '/page/1'
        Log.objects.create(type=f"STARTED", location = local, description=f"Quotes search started")
        while next_page:
            url=f'http://quotes.toscrape.com{link}'
            try:
                response=requests.get(url)
            except:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error when connecting on {url}")
            #log response
            Log.objects.create(type=f"RESPONSE", location = local, description=f"{response} when connecting on {url}")
            html=BeautifulSoup(response.text,'html.parser')
            div_tags=html.find_all('div',class_='quote')
            div_next=html.find_all('li', class_="next")
            quotes = []
            try:
                for tag in div_tags:
                    quote = tag.find('span', class_='text').text
                    quotes.append(quote)
            except:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error to find quote text on {url}")
                pass
            authors = []
            try:
                for tag in div_tags:
                    span_tag = tag.find('span', class_=None)
                    author = span_tag.find('small', class_='author').text
                    authors.append(author)
            except:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error to find author on {url}")
            name_tags = []
            try:
                for tag in div_tags:
                    name_tag = tag.find('div', class_='tags').meta['content']
                    name_tags.append(name_tag)
            except:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error to find tags on {url}")
            author_links = []
            try:
                for tag in div_tags:
                    span_tag = tag.find('span', class_=None)
                    author_link = 'http://quotes.toscrape.com' + span_tag.find('a')['href']
                    author_links.append(author_link)
            except:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error to find author_link on {url}")
            #log success
            Log.objects.create(type=f"FINISHED", location = local, description=f"Quotes returned from {url}")
            try:
                lista_quotes+=({'Quotes': quotes[i].replace(";", ":").replace("“", '"').replace("”", '"').replace("\\", ""),
                    'Author': authors[i],
                    'Tags': name_tags[i],
                    'Link': author_links[i]} for i in range(len(quotes)))
            except:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error to return the quote list from {url}")
            
            next = []
            try:
                for tag in div_next:
                    quote = tag.find('a')
                    next.append(quote['href'])
                #log success
                Log.objects.create(type=f"SUCCESS", location = local, description=f"Success to find next_page on {url}")
            except:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error to find next_page on {url}")
            if next == []:
                next_page = False
            else:
                link = next[0]
        #log success
        Log.objects.create(type=f"FINISHED", location = local, description=f"Quotes returned")
        return lista_quotes
    except:
        Log.objects.create(type=f"ERROR", location = local, description=f"General error")

def tag_quote_list(local, tag_filter):
    try:
        lista_quotes = []
        next_page = True
        link = f'/tag/{tag_filter}/page/1'
        Log.objects.create(type=f"STARTED", location = local, description=f"Quotes search started")
        while next_page:
            url=f'http://quotes.toscrape.com{link}'
            try:
                response=requests.get(url)
            except Exception as e:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error when connecting on {url}: {e}")
            #log response
            Log.objects.create(type=f"RESPONSE", location = local, description=f"{response} when connecting on {url}")
            html=BeautifulSoup(response.text,'html.parser')
            div_tags=html.find_all('div',class_='quote')
            div_next=html.find_all('li', class_="next")
            quotes = []
            try:
                for tag in div_tags:
                    quote = tag.find('span', class_='text').text
                    quotes.append(quote)
            except Exception as e:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error to find quote text on {url}: {e}")
                pass
            authors = []
            try:
                for tag in div_tags:
                    span_tag = tag.find('span', class_=None)
                    author = span_tag.find('small', class_='author').text
                    authors.append(author)
            except Exception as e:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error to find author on {url}: {e}")
            name_tags = []
            try:
                for tag in div_tags:
                    name_tag = tag.find('div', class_='tags').meta['content']
                    name_tags.append(name_tag)
            except Exception as e:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error to find tags on {url}: {e}")
            author_links = []
            try:
                for tag in div_tags:
                    span_tag = tag.find('span', class_=None)
                    author_link = 'http://quotes.toscrape.com' + span_tag.find('a')['href']
                    author_links.append(author_link)
            except Exception as e:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error to find author_link on {url}: {e}")
            #log success
            Log.objects.create(type=f"FINISHED", location = local, description=f"Quotes returned from {url}")
            try:
                lista_quotes+=({'Quotes': quotes[i].replace(";", ":").replace("“", '"').replace("”", '"').replace("\\", ""),
                    'Author': authors[i],
                    'Tags': name_tags[i],
                    'Link': author_links[i]} for i in range(len(quotes)))
            except Exception as e:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error to return the quote list from {url}: {e}")
            
            next = []
            try:
                for tag in div_next:
                    quote = tag.find('a')
                    next.append(quote['href'])
                #log success
                Log.objects.create(type=f"SUCCESS", location = local, description=f"Success to find next_page on {url}")
            except Exception as e:
                #log erro
                Log.objects.create(type=f"ERROR", location = local, description=f"Error to find next_page on {url}: {e}")
            if next == []:
                next_page = False
            else:
                link = next[0]
        #log success
        Log.objects.create(type=f"FINISHED", location = local, description=f"Quotes returned")
        return lista_quotes
    except Exception as e:
        Log.objects.create(type=f"ERROR", location = local, description=f"General error: {e}")


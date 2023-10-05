import requests
from bs4 import BeautifulSoup

'''url='http://quotes.toscrape.com/'
response=requests.get(url)
doc=BeautifulSoup(response.text,'html.parser')
div_tags=doc.find_all('div',class_='quote')'''

def list_of_dict():
    lista_quotes = []
    for i in range(1,11):
        url=f'http://quotes.toscrape.com/page/{i}'
        response=requests.get(url)
        doc=BeautifulSoup(response.text,'html.parser')
        div_tags=doc.find_all('div',class_='quote')
        quotes = []
        for tag in div_tags:
            quote = tag.find('span', class_='text').text
            quotes.append(quote)
        authors = []
        for tag in div_tags:
            span_tag = tag.find('span', class_=None)
            author = span_tag.find('small', class_='author').text
            authors.append(author)
        name_tags = []
        for tag in div_tags:
            name_tag = tag.find('div', class_='tags').meta['content']
            name_tags.append(name_tag)
        author_links = []
        for tag in div_tags:
            span_tag = tag.find('span', class_=None)
            author_link = 'http://quotes.toscrape.com' + span_tag.find('a')['href']
            author_links.append(author_link)
        lista_quotes+=({'Quotes': quotes[i],
             'Author': authors[i],
             'Tags': name_tags[i],
             'Link': author_links[i]} for i in range(len(quotes)))
    return lista_quotes
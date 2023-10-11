# Quotes to Scrape:
O site escolhido para fazer a aplicação foi o [quotes.toscrape](https://quotes.toscrape.com/). Para a aplicação foi utilizado o Django Framework, o qual eu usei para fazer uma aplicação web que busca os dados do site escolhido e depois trabalha com eles, tanto o armazenamento quanto a visualização dos dados.
Na home da aplicação tem várias opções que são divididas entre "Dados ao vivo" e "Dados do banco". As opções de dados ao vivo buscam no [quotes.toscrape](https://quotes.toscrape.com/) os dados todo momento que são acessadas e isso torna todas tarefas mais lentas, já as opções de dados do banco usam as informações armazenadas na propria aplicação, esses dados podem ser atualizados na opção "Update Database".
Tudo que acontece por trás da aplicação gera um log no banco de dados e isso pode ser acessado nas opções de "Logs e Documentação da API". Nessa sessão também pode ser acessado as documentações da api gerado pela lib Swagger.
A api foi feita com o Rest Framework e ela retorna tanto os logs quantos os dados dos quotes.
A visualização dos dados pode ser feitas pelo próprio site por templates criados a mão, templates do Pandas e também pela api Rest.
Além de visualizar o usuário consegue gerar arquivos csv e json, tanto dos quotes quanto dos logs da aplicação.
A documentação dos models pode ser encontrada na pasta root/documentacao/models-documentation.json e junto a pasta root/documentacao tem os screenshots dos dados retirados do site e também exemplos de arquivos gerados pela aplicação.
Para rodar a aplicação pode ser utilizado o Python 3.11.5 e o "requirements.txt" que está no root da aplicação. Há também a dockerfile para buildar a imagem e rodar a aplicação.

# Passo-a-Passo:

## Preparo
- Após clonar o repositório abra o terminal do pc na pasta root do projeto.
- No terminal escreva: 
- - python -m venv ./venv
- Ative o a venv
- - windows: .\venv\Scripts\activate
- - linux: Source \venv\bin\activate
- Instale os requirements:
- - pip install -r .\requirements.txt
- Crie o banco de dados local sqlite
- - python manage.py migrate

## Inicialização
- Para iniciar o programa escreva no terminal:
- - python.exe manage.py runserver
- Abra o navegador no endereço: http://localhost:8000/

# Menus
## Dados ao vivo 
Modo mais lento, pois busca os dados diretamente do [quotes.toscrape](https://quotes.toscrape.com/).
Campos:
- Quote List Generator (mostra todas as quotes disponíveis no site)
- - Botão: Generate CSV (gera um csv com todas as quotes)
- - Botão: Generate JSON (gera um json com todas as quotes)
- Tag List Generator (mostra todas as tags/filtros de quotes disponíveis no site)
- - Cada tag/filtro te leva para uma lista de quotes que tenham sua tag/filtro. Onde você pode baixar o csv e json das masmos.

## Dados do banco 
Modo mais rapido por usar dados locais do banco de dados, porém antes de usa-lo você deve usar o primeiro botão 'Update Database' e aguradar o programa buscar todas as quotes do [quotes.toscrape](https://quotes.toscrape.com/).
Campos:
- Update Database
- - Atualiza o banco de dados com as informações do do [quotes.toscrape](https://quotes.toscrape.com/).
- Quote List Generator (mostra todas as quotes disponíveis no banco de dados)
- - Botão: Generate CSV (gera um csv com todas as quotes)
- - Botão: Generate JSON (gera um json com todas as quotes)
- Tag List Generator (mostra todas as tags/filtros de quotes disponíveis no banco de dados)
- - Cada tag/filtro te leva para uma lista de quotes que tenham sua tag/filtro. Onde você pode baixar o csv e json das masmos.
- Pandas View (mostra a visualização das quotes do banco de dados por meio do Pandas.)
- Rest API (redireciona ao endereço da API que pode ser usada para ler os dados por outros programas.)

## Logs e Documentação da API
- Logs (mostra os ultimos 2000 logs de todos processos do site.)
Campos:
- - botão: Generate all log CSV (gera um csv com todos os logs do site)
- Documentação Swagger (redireciona ao endereço da documentação gerada pelo Swagger da nossa API)
- Documentação Redoc (redireciona ao endereço da documentação gerada pelo Redoc da nossa API)

# beeMôn:

Na beeMôn criamos muitos sistemas de raspagem de dados e buscamos todos os dias inovação na analise dos dados. Este desafio esta aberto para todos que quiserem abrir um fork e submeter suas ideias de tecnologia.

## Desafio:
Escolher uma dos sites abaixo para fazer o desafio

- [quotes.toscrape](https://quotes.toscrape.com/)
- [imdb.com](https://www.imdb.com/chart/top/?ref_=nv_mv_250)

### Minimo Entregável:

- Buscar dados de forma automatizada(script de linha de comando ou interface clicavel)
- Padronizar os retornos de forma estruturada (json/csv)
- Sistema de logs de para acompanhamento da execução
- Ter um prova da consulta (Screenshot)

### Pontos Extra para:

- Armazenamento dos resultados em um banco relacional ou não relacional
- fazer um dataframe que possibilite visualizar os resultados via pandas
- Trazer resultados de forma dinamica sem fixar caminhos no `xpath`
- Dockerizar a aplicação
- Conseguir agendar uma execução para um dia e horario.

### Libs sugeridas:

 - Selenium 
 - Scrapy
 - Pandas
 - Requests
 - BeautifulSoup 


### O que iremos avaliar:

- Conhecimento em HTML
- Conhecimento em fluxo de request/response
- Conhecimento em extração de dados
- Conhecimento em base64
- Boas práticas de programação
- Utilização de bibliotecas de terceiros
- Documentação
- Criatividade
- Cobertura de testes
- Tempo de execução do código
- Versionamento do código




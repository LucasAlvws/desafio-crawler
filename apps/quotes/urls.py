from django.contrib import admin
from django.urls import path,include,re_path
from .views import *
from .serializer import *
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Quotes to Scrape",
      default_version='v1',
      description="API que retorna quotes e logs do banco de dados do site principal que faz um trabalho de raspagem do site 'quotes.toscrape.com'",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('logAPI', LogListAPI, basename='logAPI')
router.register('quoteAPI', QuoteListAPI, basename='quoteAPI')
urlpatterns = [
    path('api/', include(router.urls)),
    path("", Home.as_view(), name="home"),
    path('logs/', LogList.as_view(), name="logs"),
    path('log_generate/', Log_generate.as_view(), name='log_generate'),
    path("quoteList/", QuoteList.as_view(), name="quoteList"),
    path('tagList/', TagList.as_view(), name='tagList'),
    path('tag/', TagView.as_view(), name='tagView'),
    path('csv_generate/', csv_generate.as_view(), name='csv_generate'),
    path('json_generate/', json_generate.as_view(), name='json_generate'),
    path('updateDataBase/', UpdateDataBase.as_view(), name='updateDataBase'),
    path('quoteListDB/',QuoteListDB.as_view(), name='quoteListDB'),
    path('tagViewDB/', TagViewDB.as_view(), name='tagViewDB'),
    path('tagListDB/', TagListDB.as_view(), name='tagListDB'),
    path('json_generate_db/', json_generate_db.as_view(), name='json_generate_db'),
    path('csv_generate_db/', csv_generate_db.as_view(), name='csv_generate_db'),
    path('pandas/', Pandas.as_view(), name='pandas'),   
    path('swagger/', schema_view.with_ui('swagger'), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc'), name='redoc'),
]
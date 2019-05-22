from django.urls import path
from . import views

app_name = 'articles'


urlpatterns = [
    path('', views.articles,name='list'),
    path('<slug:article_name>',views.ind_article,name='detail')
]

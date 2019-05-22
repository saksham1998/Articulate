from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse
# Create your views here.

def articles(request):
    articles = Articles.objects.all().order_by('date')
    return render(request,'articles/article_view.html',{'articles':articles})

def ind_article(request,article_name):
    article = Articles.objects.get(slug=article_name)
    return render(request,'articles/article_detail.html',{'article':article})

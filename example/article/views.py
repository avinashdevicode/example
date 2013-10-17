# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from article.models import Article

def mainView(request):
    name = 'Avinash'
    return render_to_response('main.html',{'name':name})

def mainView2(reqest):
    name= 'Avinash'
    f = get_template('main.html')
    html = f.render(Context({'name':name}))
    return  HttpResponse(html)

def allView(request):
    return render_to_response('articles.html', {'articles':Article.objects.all()})

def articleView(request, article_id=1):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id)})
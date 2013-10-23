# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from article.models import Article, Comment
from article.forms import CreateArticle, CreateComment
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone
import datetime

def mainView(request):
    name = 'Avinash'
    return render_to_response('main.html',{'name':name})

def mainView2(reqest):
    name= 'Avinash'
    f = get_template('main.html')
    html = f.render(Context({'name':name}))
    return  HttpResponse(html)

def allView(request):
    username = request.user.username
    
    return render_to_response('articles.html', {'articles':Article.objects.all(), 'username':username})

def articleView(request, article_id=1):
    username = request.user.username
    if username is not None:
        a= Article.objects.get(id = article_id)
        print a.id
        if request.POST:
            print 'Am in'
            form = CreateComment(request.POST)
            if form.is_valid():
                c = form.save(commit = False)
                c.pub_date = datetime.datetime.now()
                c.article = a
                c.save()
                return HttpResponseRedirect('/article/%s' % article_id)
        
        args_c = {}
        args_c.update(csrf(request))
        args_c['article']= a 
        args_c['comment_form'] = CreateComment()
        print 'Am in f'
        return render_to_response('article.html', args_c)
#   return render_to_response('article.html', {'article': Article.objects.get(id=article_id), 'username':username})
    
    
def createView(request):
    if request.POST:
        form = CreateArticle(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/article/all')
        
    c = {}
    c.update(csrf(request))
    c['form'] = CreateArticle()
    return render_to_response('create.html',c)

def likeView(request,article_id):
    a = Article.objects.get(id=article_id)
    count = a.likes
    count += 1
    a.likes = count
    a.save();
    return HttpResponseRedirect('/article/%s'  %article_id)

def searchTitleView(request):
    if request.POST:
        search_text = request.POST['search_text']
        
    else:
        search_text = ''
    articles = Article.objects.filter(title__contains=search_text)
    return render_to_response('search.html', {'articles': articles})

#def commentView(request, article_id):
#    a= Article.objects.get(id = article_id)
#    if request.POST:
#        print 'Am in'
#        form = CreateComment(request.POST)
#        if form.is_valid():
#            form.save(commit = False)
#            form.pub_date = timezone.now()
#            form.save()
#            return HttpResponseRedirect('/articcle/%s' % article_id)
        
#    args_c = {}
#    args_c.update(csrf(request))
#    args_c['article']= a 
#    args_c['comment_form'] = CreateComment()
#    print 'Am in f'
#    return render_to_response('article.html', args_c)
    
       
    

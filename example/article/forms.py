'''
Created on Oct 22, 2013

@author: Avi
'''
from django.forms import ModelForm
from article.models import Article
from article.models import Comment

class CreateArticle(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body', 'pub_date')
        
        
class CreateComment(ModelForm):
    class Meta:
        model= Comment
        fields = ('name', 'body')
        
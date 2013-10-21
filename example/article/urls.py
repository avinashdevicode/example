'''
Created on Oct 17, 2013

@author: Avi
'''
from django.conf.urls import include, url, patterns
import article

urlpatterns = patterns('',
                       url(r'^all/$', 'article.views.allView'),
                       url(r'^(?P<article_id>\d+)/$','article.views.articleView' ),
                       )
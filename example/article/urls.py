'''
Created on Oct 17, 2013

@author: Avi
'''
from django.conf.urls import include, url, patterns
import article

urlpatterns = patterns('',
                       url(r'^all/$', 'article.views.allView'),
                       url(r'^(?P<article_id>\d+)/$','article.views.articleView' ),
                       url(r'^create/$', 'article.views.createView'),
                       url(r'^like/(?P<article_id>\d+)/$', 'article.views.likeView'),
                       url(r'^comment/(?P<article_id>\d+)/$', 'article.views.commentView'),
                       url(r'^search_title/$', 'article.views.searchTitleView'),
                       
                       )
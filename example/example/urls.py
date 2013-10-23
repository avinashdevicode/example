from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import article.urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'article.views.mainView'),
    url(r'^hello2/$', 'article.views.mainView2'),
    url(r'article/', include(article.urls)),
    
    url(r'^accounts/login', 'example.views.loginView'),
    url(r'^accounts/auth', 'example.views.authView'),
    url(r'^accounts/logedin', 'example.views.logedinView'),
    url(r'^accounts/logout', 'example.views.logoutView'),
     url(r'^accounts/register_sucess', 'example.views.registerSuccessView'),
    url(r'^accounts/register', 'example.views.registerView', name = 'register'),
   
    
)

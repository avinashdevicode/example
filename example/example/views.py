'''
Created on Oct 17, 2013

@author: Avi
'''
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.core.context_processors import csrf
from django.contrib.auth.models import User

def loginView(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def authView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/logedin')
    else:
        return HttpResponse("Hey Wrong User Name")
    
    
def logedinView(request):
    username = request.user.username
    request.session['user_name']=username
    return render_to_response('logedin.html',{'username':username})


def logoutView(request):
    auth.logout(request)
        
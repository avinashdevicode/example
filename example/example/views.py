'''
Created on Oct 17, 2013

@author: Avi
'''
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate

def loginView(request):
    return render_to_response('login.html')

def authView(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    
    user = authenticate(username=username,password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/logedin')
    else:
        return HttpResponseRedirect('accounts/invalid')
        
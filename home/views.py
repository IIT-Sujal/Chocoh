# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import start_user_session,check_if_auth_user,stop_user_session

# Create your views here.
def homepage(request):
	ContextData={}
	if check_if_auth_user(request):
		ContextData['user']=check_if_auth_user(request)
	else:
		ContextData['user']=None;

	return render(request, 'home.html',ContextData)
def register(request):

	return render(request, 'home.html',{})
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib import messages
import MySQLdb

# Create your views here.
db=MySQLdb.connect(host="localhost",user="root",passwd="trisha",db="chocoh")
cur=db.cursor()
def homepage(request):
	ContextData={'product_quantity':range(0,6)}
	return render(request, 'home.html',ContextData)

def signup(request):
	name=request.POST.get('usr')
	email_id=request.POST.get('email')
	contact_no=request.POST.get('contact')
	password=request.POST.get('pwd')
	if name and email_id and contact_no and password:
	 	messages.success(request, "Successful Signup!")
	 	query="INSERT INTO user(name,password,email_id,contact_no) values('%s','%s','%s','%s');"%(name,password,email_id,contact_no)
		cur.execute(query)
		db.commit(); 	
	 	return redirect("login")
	else:
		return render(request, 'signup.html',{})

def login(request):
	ContextData={}
	ContextData['x']=0
	email_id=request.POST.get('email_id')
	password=request.POST.get('password')
	if email_id and password:
		query="select email_id,password from user where email_id='%s' and password='%s'"%(email_id,password)
		cur.execute(query)
		l=cur.fetchall()
		if l:
			request.session['user_id']=l[0]
			messages.success(request,"Successful Login")
			return redirect("homepage")
		else:
			messages.error(request,"Invalid Email-Id or Password!")
			return render(request, 'login.html',ContextData)	
	else:
		return render(request, 'login.html',ContextData)
def logout(request):
	del request.session['user_id']
	return redirect ("homepage")
def cart(request):

	return render(request,'cart.html',{})

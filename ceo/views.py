# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib import messages
import MySQLdb
from home.views import db_init
# Create your views here.
def delete_user(request,pk):
	db,cur=db_init()
	query="delete from user where user_id='%s'"%(pk);
	cur.execute(query)
	db.commit()
	return redirect("ceouser")
def homepage(request):
	db,cur=db_init()
	query="select * from chocolate";
	cur.execute(query)
	product_list=cur.fetchall()
	ContextData={'product_quantity':range(0,len(product_list)),'product_list':product_list}
	return render(request, 'home.html',ContextData)

def ceoorderpast(request):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		query="select * from orders where order_status='completed'";
		cur.execute(query)
		ContextData={}
		ContextData['orders']=cur.fetchall()
		ContextData['status']='past'
		return render(request, 'ceoorder.html',ContextData)
	else:
		return redirect("ceologin")

def ceoorder(request):	
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		query="select * from orders where order_status='pending'";
		cur.execute(query)
		ContextData={}
		ContextData['orders']=cur.fetchall()
		ContextData['status']='current'
		return render(request, 'ceoorder.html',ContextData)
	else:
		return redirect("ceologin")

def login(request):
	db,cur=db_init()
	ContextData={}
	ContextData['x']=0
	email_id=request.POST.get('email_id')
	password=request.POST.get('password')
	if email_id and password:
		query="select ceo_id from ceo where email_id='%s' and password='%s'"%(email_id,password)
		cur.execute(query)
		l=cur.fetchall()
		if l:
			request.session['ceo_id']=l[0][0]
			messages.success(request,"Successful Login")
			return redirect("ceohome")
		else:
			messages.error(request,"Invalid Email-Id or Password!")
			return render(request, 'ceologin.html',ContextData)	
	else:
		return render(request, 'ceologin.html',ContextData)
def logout(request):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		del request.session['ceo_id']
	return redirect ("ceologin")
def ceouser(request):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		query="select * from user";
		cur.execute(query)
		ContextData={}
		ContextData['user']=cur.fetchall()
		return render(request, 'ceouser.html',ContextData)
	else:
		return redirect("ceologin")
def ceofeedback(request):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		query="select * from feedback";
		cur.execute(query)
		ContextData={}
		ContextData['feedback']=cur.fetchall()
		return render(request, 'ceofeedback.html',ContextData)
	else:
		return redirect("ceologin")
def shipper_info(request):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		query="select * from shipper_info";
		cur.execute(query)
		ContextData={}
		ContextData['shipper_info']=cur.fetchall()
		return render(request, 'ceoshipper_info.html',ContextData)
	else:
		return redirect("ceologin")
def ceoproducts(request):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		query="select * from chocolate";
		cur.execute(query)
		ContextData={}
		ContextData['chocolate']=cur.fetchall()
		return render(request, 'ceoshipper_info.html',ContextData)
	else:
		return redirect("ceologin")
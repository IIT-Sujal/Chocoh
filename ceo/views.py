# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib import messages
import MySQLdb
import hashlib
from home.views import db_init
from django.core.files.storage import FileSystemStorage
from base64 import b64encode
# Create your views here.
def delete_user(request,pk):
	db,cur=db_init()
	query="delete from user where user_id='%s'"%(pk)
	cur.execute(query)
	db.commit()
	return redirect("ceouser")
def homepage(request):
	db,cur=db_init()
	query="select * from chocolate"
	cur.execute(query)
	product_list=cur.fetchall()
	ContextData={'product_quantity':range(0,len(product_list)),'product_list':product_list}
	return render(request, 'home.html',ContextData)

def ceoorderpast(request):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		query="select * from orders where order_status='completed'"
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
		query="select * from orders where order_status='pending'"
		cur.execute(query)
		ContextData={}
		ContextData['orders']=cur.fetchall()
		ContextData['status']='current'
		return render(request, 'ceoorder.html',ContextData)
	else:
		return redirect("ceologin")

def login(request):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		return redirect("ceohome")
	else:
		ContextData={}
		ContextData['x']=0
		email_id=request.POST.get('email_id')
		password=request.POST.get('password')
		if email_id and password:
			query="select * from ceo where email_id='%s' and password='%s'"%(email_id,hashlib.md5(password.encode('utf8')).hexdigest())
			cur.execute(query)
			l=cur.fetchall()
			if l:
				request.session['ceo_id']=l[0][1]
				request.session['ceo_password']=l[0][2]
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
		del request.session['ceo_password']
	return redirect ("ceologin")
def ceouser(request):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		query="select * from user"
		cur.execute(query)
		ContextData={}
		ContextData['user']=cur.fetchall()
		return render(request, 'ceouser.html',ContextData)
	else:
		return redirect("ceologin")
def ceofeedback(request):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		query="select * from feedback"
		cur.execute(query)
		ContextData={}
		ContextData['feedback']=cur.fetchall()
		return render(request, 'ceofeedback.html',ContextData)
	else:
		return redirect("ceologin")
def shipper_info(request):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		query="select * from shipper_info"
		cur.execute(query)
		ContextData={}
		ContextData['shipper_info']=cur.fetchall()
		return render(request, 'ceoshipper_info.html',ContextData)
	else:
		return redirect("ceologin")
def ceoproducts(request):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		query="select * from chocolate"
		cur.execute(query)
		ContextData={}
		ContextData['chocolate']=cur.fetchall()
		return render(request, 'ceoproducts.html',ContextData)
	else:
		return redirect("ceologin")
def delete_from_product(request,pk):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		try:
			query="Delete from chocolate where chocolate_id='%s'"%(pk)
			cur.execute(query)
			db.commit()
		except:
			messages.success(request,"You cannot delete this product. It has been ordered by some user.")
		return redirect("ceoproducts")
	else:
		return redirect("ceologin")

def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo 

def add_to_products(request):
	db,cur=db_init()
	if request.session.has_key('ceo_id'):
		price=request.POST.get("price")
		name=request.POST.get("name")
		quantity_available=request.POST.get("quantity_available")
		description=request.POST.get("description")
		ratings=request.POST.get("ratings")
		if price and name and quantity_available and description and ratings:
			if len(request.FILES) != 0:
				image = request.FILES["product_image"].read()	
				image=b64encode(image)
				query="insert into chocolate(name,price,quantities_available,quantities_sold,ratings,image) values(%s,%s,%s,%s,%s,%s)"
				args=(name,price,quantity_available,0,ratings,image)
				cur.execute(query,args)
				db.commit()
				return redirect("ceoproducts")
			else:
				query="insert into chocolate(name,price,quantities_available,quantities_sold,ratings) values(%s,%s,%s,%s,%s)"
				args=(name,price,quantity_available,0,ratings)
				cur.execute(query,args)
				db.commit()
				return redirect("ceoproducts")
		else:
			return render(request, 'addproducts.html')
	else:
		return redirect("ceologin")
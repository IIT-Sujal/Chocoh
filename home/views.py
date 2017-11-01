# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib import messages
import MySQLdb,payu_biz,uuid
from payu_biz.views import make_transaction

# Create your views here.
def db_init():
	db=MySQLdb.connect(host="sujal24.mysql.pythonanywhere-services.com",user="sujal24",passwd="Goldman@123",db="sujal24$chocoh")
	return db,db.cursor()

def get_txnid():
	db,cur=db_init()
	txnid="ctxn"+str(uuid.uuid4())
	query="select * from payment where payment_id='%s'"%(txnid)
	cur.execute(query)
	l=cur.fetchall()
	if l :
		return get_txnid()
	else :
		return txnid

def homepage(request):
	db,cur=db_init()
	query="select * from chocolate";
	cur.execute(query)
	product_list=cur.fetchall()
	ContextData={'product_quantity':range(0,len(product_list)),'product_list':product_list}
	return render(request, 'home.html',ContextData)

def signup(request):
	db,cur=db_init()
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
def contact(request):
	db,cur=db_init()
	name=request.POST.get('name')
	email=request.POST.get('email')
	contact_no=request.POST.get('contact')
	user_message=request.POST.get('message')
	print name,email,contact_no,user_message
	if name and email and contact_no :
		query="insert into messages(name,email_id,contact_no,messages) values('%s','%s','%s','%s')"%(name,email,contact_no,user_message)
		cur.execute(query)
		db.commit()
		messages.success(request,"Your Message has reached us. We will reach you out shortly.")
		return redirect("homepage")
	else:
		messages.success(request,"Please fill the form properly to get in touch with us.")
		return redirect("homepage")


def login(request):
	if request.session.has_key('user_id'):
		messages.success(request, "Already Logged in!")
		return redirect("homepage")
	db,cur=db_init()
	ContextData={}
	ContextData['x']=0
	email_id=request.POST.get('email_id')
	password=request.POST.get('password')
	if email_id and password:
		query="select user_id from user where email_id='%s' and password='%s'"%(email_id,password)
		cur.execute(query)
		l=cur.fetchall()
		if l:
			request.session['user_id']=l[0][0]
			messages.success(request,"Successful Login")
			return redirect("homepage")
		else:
			messages.error(request,"Invalid Email-Id or Password!")
			return render(request,'login.html',ContextData)	
	else:
		return render(request, 'login.html',ContextData)
def logout(request):
	db,cur=db_init()
	if request.session.has_key('user_id'):
		del request.session['user_id']
	return redirect ("homepage")
def cart(request,pk,quantity_update):
	db,cur=db_init()
	if request.session.has_key('user_id'):
		if pk!='0':
			print 'rajputana',request.session['user_id']
			query="select * from user_cart where user_id='%s' and chocolate_id='%s'"%(request.session['user_id'],pk) 
			cur.execute(query)
			already_bought=cur.fetchall()
			if already_bought:
				if quantity_update=='0':
					quantity=already_bought[0][2]+1
				else:
					quantity=request.POST.get('quantity')
					query="DELETE FROM user_cart where user_id='%s' and chocolate_id='%s'"%(request.session['user_id'],pk) 
					cur.execute(query)
					query="INSERT INTO user_cart(user_id,chocolate_id,quantity) values('%s','%s','%s')"%(request.session['user_id'],pk,quantity)
					cur.execute(query)
					db.commit()
					return redirect("cart", pk='0',quantity_update='0')
				query="DELETE FROM user_cart where user_id='%s' and chocolate_id='%s'"%(request.session['user_id'],pk) 
				cur.execute(query)
				query="INSERT INTO user_cart(user_id,chocolate_id,quantity) values('%s','%s','%s')"%(request.session['user_id'],pk,quantity)
				cur.execute(query)
			else:
				query="INSERT INTO user_cart(user_id,chocolate_id) values('%s','%s')"%(request.session['user_id'],pk) 
				cur.execute(query)
			db.commit()
			messages.success(request,"added to cart successfully")
			return redirect('/home#productpage')
		else:
			query="Select * from user_cart,chocolate where user_id='%s' and user_cart.chocolate_id=chocolate.chocolate_id"%(request.session['user_id']) 
			cur.execute(query)
			cart=cur.fetchall()
			price=0
			for i in cart:
				price+=i[2]*i[4]
			return render(request, 'cart.html',{'cart':cart,'price':price})
	else:
		return redirect("login")
def delete_from_cart(request,pk):
	db,cur=db_init()
	query="DELETE FROM user_cart where user_id='%s' and chocolate_id='%s'"%(request.session['user_id'],pk) 
	cur.execute(query)
	db.commit()
	return redirect('/cart/0/0')
def chocolate_detail(request,pk):
	db,cur=db_init()
	query="SELECT * from chocolate where chocolate_id='%s'"%(pk)
	cur.execute(query)
	l=cur.fetchall()
	return render(request, 'product_detail.html',{'product':l[0]})
def payment(request):
	db,cur=db_init()
def delivery(request):
	price=request.POST.get('price')
	name=request.POST.get('name')
	email=request.POST.get('email')
	contact_no=request.POST.get('contact_no')
	ad1=request.POST.get('address_line_1')
	ad2=request.POST.get('address_line_2')
	pincode=request.POST.get('pincode')
	print 'hi',price,name,email,contact_no,ad1,ad2,pincode
	if price and name and email and contact_no and ad1 and pincode:
		ContextData={}
		ContextData['txnid']=get_txnid()
		ContextData['amount']=price
		ContextData['productinfo']='chocolate'
		ContextData['firstname']=name
		ContextData['phone']=contact_no
		ContextData['email']=email
		return make_transaction(ContextData)
	elif price :
		amount=request.POST.get('amount')
		return render(request,'delivery.html',{'price':price})
	else:
		messages.success(request, "Please fill the details completely.")
		return render(request,'delivery.html')
def success(request):
	db,cur=db_init()
	query="Select * from user_cart where user_id='%s'"%(request.session.get('user_id'))
	cur.execute(query)
	order_list=cur.fetchall()
	query="Delete from user_cart where user_id='%s'"%(request.session.get('user_id'))
	cur.execute(query)
	messages.success(request, "Your Payment is successful and your order has been placed.")
	return redirect("homepage")
def failure(request):
	messages.success(request, "Your Payment has been failed. In case your amount has been deducted sit back and relax. It will refunded to your account in 7-10 working days.")
	return redirect("homepage")

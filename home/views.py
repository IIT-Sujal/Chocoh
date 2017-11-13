# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import hashlib
from django.shortcuts import render,redirect,reverse,render_to_response
from django.contrib import messages
import MySQLdb,uuid,hashlib
import home.constants as constants,home.config as config
from random import randint
# Create your views here.
def db_init():
	db=MySQLdb.connect(host="localhost",user="sujal24",passwd="abc123abc",db="sujal24$chocoh")
	return db,db.cursor()

def homepage(request):
	db,cur=db_init()
	query="select * from chocolate";
	cur.execute(query)
	product_list=cur.fetchall()
	ContextData={'product_quantity':range(0,len(product_list)),'product_list':product_list}
	return render(request, 'home.html',ContextData)
 
# create hash string using all the fields


def signup(request):
	db,cur=db_init()
	name=request.POST.get('usr')
	email_id=request.POST.get('email')
	contact_no=request.POST.get('contact')
	password=request.POST.get('pwd')
	if name and email_id and contact_no and password:
	 	messages.success(request, "Successful Signup!")
	 	query="INSERT INTO user(name,password,email_id,contact_no) values('%s','%s','%s','%s');"%(name,hashlib.md5(password.encode('utf8')).hexdigest(),email_id,contact_no)
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
		query="select user_id from user where email_id='%s' and password='%s'"%(email_id,hashlib.md5(password.encode('utf8')).hexdigest())
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
		posted={}
		posted["amount"]=price
		posted["email"]=email
		posted["firstname"]=name
		posted["productinfo"]='chocolate'
		posted["surl"]="sujal24.pythonanywhere.com/success"
		posted["furl"]="sujal24.pythonanywhere.com/failure"
		ContextData['posted']=posted		
		ContextData['action']='/payment'
		return render(request,'payment.html',ContextData)
	elif price :
		amount=request.POST.get('amount')
		return render(request,'delivery.html',{'price':price})

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
def payment(request):
	MERCHANT_KEY = "u2bLZsT6"
	key="u2bLZsT6"
	SALT = "Jb8UjE9prK"
	PAYU_BASE_URL = "https://secure.payu.in/_payment"
	action = ''
	posted={}
	for i in request.POST:
		print "hi",i
		posted[i]=request.POST[i]
	hash_object = hashlib.sha256(b'randint(0,20)')
	txnid=hash_object.hexdigest()[0:20]
	hashh = ''
	posted['txnid']=txnid
	hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
	posted['key']=key
	hash_string=''
	hashVarsSeq=hashSequence.split('|')
	for i in hashVarsSeq:
		try:
			hash_string+=str(posted[i])
		except Exception:
			hash_string+=''
		hash_string+='|'
	hash_string+=SALT
	print "woo",hash_string,"woo"
	hashh=hashlib.sha512(hash_string).hexdigest().lower()
	print "hii",hashh
	action =PAYU_BASE_URL
	if(posted.get("key")!=None and posted.get("txnid")!=None and posted.get("productinfo")!=None and posted.get("firstname")!=None and posted.get("email")!=None):
		return render_to_response('payment.html',{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"https://secure.payu.in/_payment" })
	else:
		return render_to_response('payment.html',{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"." })
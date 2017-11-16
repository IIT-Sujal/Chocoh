# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import hashlib
from django.shortcuts import render,redirect,reverse,render_to_response
from django.contrib import messages
from django.template import Context, Template,RequestContext
import MySQLdb,uuid,hashlib
import home.constants as constants,home.config as config
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from random import randint
# Create your views here.
#sujal24.mysql.pythonanywhere-services.com
def db_init():
	db=MySQLdb.connect(host=constants.host,user="sujal24",passwd="abc123abc",db="sujal24$chocoh")
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

def get_quantity(chocolate_id):
	db,cur=db_init()
	query="Select quantities_available from chocolate where chocolate_id='%s'"%(str(chocolate_id))
	cur.execute(query)
	l=cur.fetchall()
	return int(l[0][0])

def change_quantity(chocolate_id,quantity):
	db,cur=db_init()
	query="update chocolate set quantities_available='%s'where chocolate_id='%s'"%(str(quantity),str(chocolate_id))
	cur.execute(query)
	db.commit()
	return None

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
					quantity=int(request.POST.get('quantity'))
					available=get_quantity(pk)
					print "hi", available
					if available>=quantity:
						query="DELETE FROM user_cart where user_id='%s' and chocolate_id='%s'"%(request.session['user_id'],pk) 
						cur.execute(query)
						query="INSERT INTO user_cart(user_id,chocolate_id,quantity) values('%s','%s','%s')"%(request.session['user_id'],pk,quantity)
						cur.execute(query)
						db.commit()
						return redirect("cart", pk='0',quantity_update='0')
					else:
						messages.success(request,"Sorry, We don't have the required quantity.")
						return redirect("homepage")
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
		posted["surl"]="https://sujal24.pythonanywhere.com/success"
		posted["furl"]="https://sujal24.pythonanywhere.com/failure"
		ContextData['posted']=posted		
		ContextData['action']='/payment'
		print ":dsjjdsdh"
		return payment(request, posted)
	elif price :
		amount=request.POST.get('amount')
		return render(request,'delivery.html',{'price':price})

@csrf_protect
@csrf_exempt
def success(request):
	c = {}
   	c.update(csrf(request))
	status=request.POST["status"]
	firstname=request.POST["firstname"]
	amount=request.POST["amount"]
	txnid=request.POST["txnid"]
	posted_hash=request.POST["hash"]
	key=request.POST["key"]
	productinfo=request.POST["productinfo"]
	email=request.POST["email"]
	salt=constants.SALT
	try:
		additionalCharges=request.POST["additionalCharges"]
		retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	except Exception:
		retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
	if(hashh !=posted_hash):
		print "Invalid Transaction. Please try again"
	else:
		print "Thank You. Your order status is ", status
		print "Your Transaction ID for this transaction is ",txnid
		print "We have received a payment of Rs. ", amount ,". Your order will soon be shipped."
		messages.success(request, "Your order has been placed")
	return redirect("homepage")

@csrf_protect
@csrf_exempt
def failure(request):
	c = {}
    	c.update(csrf(request))
	status=request.POST["status"]
	firstname=request.POST["firstname"]
	amount=request.POST["amount"]
	txnid=request.POST["txnid"]
	posted_hash=request.POST["hash"]
	key=request.POST["key"]
	productinfo=request.POST["productinfo"]
	email=request.POST["email"]
	salt= constants.SALT
	try:
		additionalCharges=request.POST["additionalCharges"]
		retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	except Exception:
		retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
	if(hashh !=posted_hash):
		print "Invalid Transaction. Please try again"
	else:
		messages.success(request, "Your Payment has been failed. Your order has turned into COD.")
 	return redirect("homepage")

def payment(request,posted):
	db,cur=db_init()
	query="select chocolate_id,quantity from user_cart where user_id='%s'"%(request.session['user_id'])
	cur.execute(query)
	l=cur.fetchall()
	check=True
	for i in l:
		if int(i[1])>get_quantity(i[0]):
			check=False
	if check==False:
		messages.success(request,"Some of your cart item is out of stock please remove that from cart.")
		return redirect("homepage")
	else:
		for i in l:
			change_quantity(i[0], get_quantity(i[0])-i[1])
	MERCHANT_KEY = constants.KEY
	key=constants.KEY 
	SALT = constants.SALT 
	PAYU_BASE_URL = constants.PAYMENT_URL_LIVE
	action = ''
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
	hashh=hashlib.sha512(hash_string).hexdigest().lower()
	action =PAYU_BASE_URL
	return render_to_response('payment.html',{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":constants.PAYMENT_URL_LIVE })
from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template,RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf

@csrf_protect
@csrf_exempt
def Home(request):
	MERCHANT_KEY = "u2bLZsT6"
	key="u2bLZsT6"
	SALT = "Jb8UjE9prK"
	PAYU_BASE_URL = "https://secure.payu.in/_payment"
	action = ''
	posted={}
	for i in request.POST:
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
		return render_to_response('current_datetime.html',{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"https://secure.payu.in/_payment" })
	else:
		return render_to_response('current_datetime.html',{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"." })

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
	salt="GQs7yium"
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
	return render_to_response('sucess.html',RequestContext(request,{"txnid":txnid,"status":status,"amount":amount}))


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
	salt="GQs7yium"
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
 	return render_to_response("Failure.html",RequestContext(request,c))

	

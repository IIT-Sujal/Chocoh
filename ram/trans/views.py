from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from payu_biz.views import make_transaction
from django.http import JsonResponse # django version 1.10
from uuid import uuid4

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import OrderForm

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from shoeshowroom.models import product,relation,querysub
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def payment(request,username):
	# Amount Calculaion
	userx=get_object_or_404(User,username=username)
	every=relation.objects.all()
	all_products=product.objects.all()
	list1=[i.productid for i in every if i.userid==userx.username]
	list_of_products=[i for i in all_products if i.myid in list1]
	quantity_product=[]
	for i in list_of_products:
		for j in every:
			if(i.myid==j.productid and userx.username==j.userid):
				quantity_product.append(j.quantity)
				break
	product_quan=[[list_of_products[i],quantity_product[i]] for i in range(len(list_of_products))]
	tpr=0
	dvc=0
	tc=0
	for i in product_quan:
		tpr=tpr+i[0].price*i[1];
	if tpr<200:
		dvc=49
	tc=dvc+tpr
	amount=tc

	# Form Part
	if request.method == 'POST':
		form=OrderForm(request.POST)
		if form.is_valid():
			txnid=str(uuid4())
			firstname=form.cleaned_data.get('firstname')
			lastname=form.cleaned_data.get('lastname')
			email=form.cleaned_data.get('email')
			phone=form.cleaned_data.get('phone')
			address1=form.cleaned_data.get('address1')
			address2=form.cleaned_data.get('address2')
			city=form.cleaned_data.get('city')
			state=form.cleaned_data.get('state')
			country=form.cleaned_data.get('country')
			zipcode=form.cleaned_data.get('zipcode')

			cleaned_data={'txnid':txnid,'amount':amount,'productinfo':"alpha",'firstname':firstname,'lastname':lastname,'email':email,
				'phone':phone,'address1'
				:address1,'address2':address2,'city':city,'state':state,'country':country,'zipcode':zipcode,'udf1':'','udf2':'','udf3':'','udf4':'','udf5':'',
				'udf6':'','udf7':'','udf8':'','udf9':'','udf10':''
			}
			
			return make_transaction(cleaned_data)


	else:
		form=OrderForm
		return render(request, 'trans/payment.html', {'form': form,'amount':amount})


@csrf_exempt
def payu_success(request):
    return JsonResponse(request.POST)
@csrf_exempt
def payu_failure(request):
    return JsonResponse(request.POST)
@csrf_exempt
def payu_cancel(request):
    return JsonResponse(request.POST)
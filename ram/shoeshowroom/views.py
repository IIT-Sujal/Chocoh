from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import product,relation,querysub
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


# Create your views here.
def tquery(request):
	if request.method=="POST":
		print "hie"
		namex=request.POST['name']
		emailx=request.POST['email']
		queryx=request.POST['query']
		queryentry=querysub(name=namex,email=emailx,query=queryx)
		queryentry.save()
		queries=querysub.objects.all()
		return render(request,'shoeshowroom/query.html',{'queries':queries})
	else:
		return render(request,'shoeshowroom/tquery.html',{})

def query(request):
	queries=querysub.objects.all()
	print queries
	return render(request,'shoeshowroom/query.html',{'queries':queries})

def men_sec(request):
	all_products=product.objects.all()
	list1=[i for i in all_products if i.category=='M']
	all_products=list1
	return render(request,'shoeshowroom/filtered.html',{'all_products':all_products})

def women_sec(request):
	all_products=product.objects.all()
	list1=[i for i in all_products if i.category=='F']
	all_products=list1
	return render(request,'shoeshowroom/filtered.html',{'all_products':all_products})

def kids_sec(request):
	all_products=product.objects.all()
	list1=[i for i in all_products if i.category=='K']
	all_products=list1
	return render(request,'shoeshowroom/filtered.html',{'all_products':all_products})


def filter(request):
	if request.method=="POST":
		fgender=request.POST.getlist('gender')
		fcollection=request.POST.getlist('collection')
		fsize=request.POST.getlist('size')
		minval=request.POST.get('minval')
		maxval=request.POST.get('maxval')
		all_products=product.objects.all()
		if len(fgender)>0:
			list1=[i for i in all_products if i.category in fgender]
			all_products=list1
		if len(fcollection)>0:
			list1=[i for i in all_products if i.floater in fcollection]
			all_products=list1
		if len(fsize)>0:
			alpha=[int(i) for i in fsize]
			print alpha
			list1=[]
			for i in all_products:
				if i.size6==1 and (6 in alpha):
					list1.append(i)
					continue
				if i.size7==1 and (7 in alpha):
					list1.append(i)
					continue
				if i.size8==1 and (8 in alpha):
					list1.append(i)
					continue
				if i.size9==1 and (9 in alpha):
					list1.append(i)
					continue
				if i.size10==1 and (10 in alpha):
					list1.append(i)
					continue
			all_products=list1
		if minval:
			mi=int(minval)
			list1=[i for i in all_products if i.price>=mi]
			all_products=list1
		if maxval:
			ma=int(maxval)
			if(ma!=4000):
				list1=[i for i in all_products if i.price<=ma]
				all_products=list1
		return render(request,'shoeshowroom/filtered.html',{'all_products':all_products})
	else:
		return render(request, 'shoeshowroom/filter.html',{})

def home(request):
	list_of_products=product.objects.all()
	return render(request, 'shoeshowroom/home.html', {'list_of_products':list_of_products})

def details(request,pk):
	productx=get_object_or_404(product,pk=pk)
	return render(request,"shoeshowroom/details.html",{'productx':productx})




@login_required
def cart(request,username):
	userx=get_object_or_404(User,username=username)
	every=relation.objects.all()
	all_products=product.objects.all()
	list1=[[i.productid,i.size,i.quantity,i.relid] for i in every if i.userid==userx.username]
	product_quan=[]
	for i in list1:
		for j in all_products:
			if(i[0]==j.myid):
				product_quan.append([j,i[2],i[1],i[3]])
	tpr=0
	dvc=0
	tc=0
	for i in product_quan:
		tpr=tpr+i[0].price*i[1];
	if tpr<600 and tpr>0:
		dvc=49
	tc=dvc+tpr
	if tpr>0:
		return render(request,"shoeshowroom/cart.html",{'product_quan':product_quan,'tpr':tpr,'dvc':dvc,'tc':tc})
	else:
		return render(request,"shoeshowroom/emptycart.html",{})

@login_required
def add_to_cart10(request,pk,username):
	userx=get_object_or_404(User,username=username)
	productx=get_object_or_404(product,pk=pk)
	every=relation.objects.all()
	flag=0
	rel_temp=relation(userid=userx.username,productid=productx.myid,size=10,quantity=1)
	for i in every:
		if(i.userid==userx.username and i.productid==productx.myid and i.size==10):
			flag=1
			rel_temp=i
			break

	if flag:
		rel_temp.quantity+=1
		rel_temp.save()
		return render(request,"shoeshowroom/thank.html",{})

	cartentry=relation(userid=userx.username,productid=productx.myid,size=10,quantity=1)
	cartentry.save()
	return render(request,"shoeshowroom/thank.html",{})

def add_to_cart9(request,pk,username):
	userx=get_object_or_404(User,username=username)
	productx=get_object_or_404(product,pk=pk)
	every=relation.objects.all()
	flag=0
	rel_temp=relation(userid=userx.username,productid=productx.myid,size=9,quantity=1)
	for i in every:
		if(i.userid==userx.username and i.productid==productx.myid and i.size==9):
			flag=1
			rel_temp=i
			break

	if flag:
		rel_temp.quantity+=1
		rel_temp.save()
		return render(request,"shoeshowroom/thank.html",{})

	cartentry=relation(userid=userx.username,productid=productx.myid,size=9,quantity=1)
	cartentry.save()
	return render(request,"shoeshowroom/thank.html",{})

def add_to_cart8(request,pk,username):
	userx=get_object_or_404(User,username=username)
	productx=get_object_or_404(product,pk=pk)
	every=relation.objects.all()
	flag=0
	rel_temp=relation(userid=userx.username,productid=productx.myid,size=8,quantity=1)
	for i in every:
		if(i.userid==userx.username and i.productid==productx.myid and i.size==8):
			flag=1
			rel_temp=i
			break

	if flag:
		rel_temp.quantity+=1
		rel_temp.save()
		return render(request,"shoeshowroom/thank.html",{})

	cartentry=relation(userid=userx.username,productid=productx.myid,size=8,quantity=1)
	cartentry.save()
	return render(request,"shoeshowroom/thank.html",{})

def add_to_cart7(request,pk,username):
	userx=get_object_or_404(User,username=username)
	productx=get_object_or_404(product,pk=pk)
	every=relation.objects.all()
	flag=0
	rel_temp=relation(userid=userx.username,productid=productx.myid,size=7,quantity=1)
	for i in every:
		if(i.userid==userx.username and i.productid==productx.myid and i.size==7):
			flag=1
			rel_temp=i
			break

	if flag:
		rel_temp.quantity+=1
		rel_temp.save()
		return render(request,"shoeshowroom/thank.html",{})

	cartentry=relation(userid=userx.username,productid=productx.myid,size=7,quantity=1)
	cartentry.save()
	return render(request,"shoeshowroom/thank.html",{})

def add_to_cart6(request,pk,username):
	userx=get_object_or_404(User,username=username)
	productx=get_object_or_404(product,pk=pk)
	every=relation.objects.all()
	flag=0
	rel_temp=relation(userid=userx.username,productid=productx.myid,size=6,quantity=1)
	for i in every:
		if(i.userid==userx.username and i.productid==productx.myid and i.size==6):
			flag=1
			rel_temp=i
			break

	if flag:
		rel_temp.quantity+=1
		rel_temp.save()
		return render(request,"shoeshowroom/thank.html",{})

	cartentry=relation(userid=userx.username,productid=productx.myid,size=6,quantity=1)
	cartentry.save()
	return render(request,"shoeshowroom/thank.html",{})



def remove_from_cart(request,pk):
	rel=get_object_or_404(relation,pk=pk)
	every=relation.objects.all()
	for i in every:
		if(i.relid==rel.relid):
			i.delete()
			break

	return render(request,"shoeshowroom/removed.html",{})

def payment(request,username):
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
	return render(request,"shoeshowroom/payment.html",{'product_quan':product_quan,'tpr':tpr,'dvc':dvc,'tc':tc})


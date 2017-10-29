from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
	#url(r'^accounts/login/$', auth_views.login, {'template_name': 'Election_Portal/login.html'},name='login'),
	url(r'^filter/$',views.filter,name='filter'),
	url(r'^$',views.home,name='home'),
	url(r'^home/$',views.home,name='home'),
	url(r'^details/(?P<pk>\d+)/$',views.details,name='details'),
	url(r'^cart/(?P<username>[\w.@+-]+)/$',views.cart,name='cart'),
	url(r'^add_to_cart6/(?P<pk>\d+)/(?P<username>[\w.@+-]+)/$',views.add_to_cart6,name='add_to_cart6'),
	url(r'^add_to_cart7/(?P<pk>\d+)/(?P<username>[\w.@+-]+)/$',views.add_to_cart7,name='add_to_cart7'),
	url(r'^add_to_cart8/(?P<pk>\d+)/(?P<username>[\w.@+-]+)/$',views.add_to_cart8,name='add_to_cart8'),
	url(r'^add_to_cart9/(?P<pk>\d+)/(?P<username>[\w.@+-]+)/$',views.add_to_cart9,name='add_to_cart9'),
	url(r'^add_to_cart10/(?P<pk>\d+)/(?P<username>[\w.@+-]+)/$',views.add_to_cart10,name='add_to_cart10'),
	url(r'^remove_from_cart/(?P<pk>\d+)/$',views.remove_from_cart,name='remove_from_cart'),
	url(r'^men_sec/',views.men_sec,name='men_sec'),
	url(r'^women_sec/',views.women_sec,name='women_sec'),
	url(r'^kids_sec/',views.kids_sec,name='kids_sec'),
	url(r'^query/',views.query,name='query'),
	url(r'^tquery/',views.tquery,name='tquery'),
	

]
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.homepage,name='homepage'),
	url(r'^home', views.homepage,name='homepage'),
	url(r'^signup$', views.signup,name='signup'),
	url(r'^login$', views.login,name='login'),
	url(r'^logout/$', views.logout,name='logout'),
	url(r'^cart/(?P<pk>[0-9]+)/(?P<quantity_update>[0-9]+)$', views.cart,name='cart'),
	url(r'^delete_from_cart/(?P<pk>[0-9]+)$', views.delete_from_cart,name='delete_from_cart'),
	url(r'^product_detail/(?P<pk>[0-9]+)$', views.chocolate_detail,name='chocolate_detail'),
	url(r'^contact_us_message$', views.contact,name='contact'),
	url(r'^makepayment$', views.payment,name='payment'),
	url(r'^delivery_details$', views.delivery,name='delivery'),
	url(r'^success$', views.success,name='success'),
	url(r'^failure$', views.failure,name='failure'),
	url(r'^payment$', views.payment,name='payment'),
]
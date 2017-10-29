from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.homepage,name='homepage'),
	url(r'^home', views.homepage,name='homepage'),
	url(r'^signup$', views.signup,name='signup'),
	url(r'^login$', views.login,name='login'),
	url(r'^logout/$', views.logout,name='logout'),
	url(r'^cart/(?P<pk>[0-9]+)$', views.cart,name='cart'),
	url(r'^delete_from_cart/(?P<pk>[0-9]+)$', views.delete_from_cart,name='delete_from_cart'),
	url(r'^product_detail/(?P<pk>[0-9]+)$', views.chocolate_detail,name='chocolate_detail'),
]
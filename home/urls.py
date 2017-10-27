from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home', views.homepage,name='homepage'),
	url(r'^signup$', views.signup,name='signup'),
	url(r'^login$', views.login,name='login'),
	url(r'^logout$', views.logout,name='logout'),
	url(r'^cart$', views.cart,name='cart'),
]
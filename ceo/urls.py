from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home', views.ceoorder,name='ceohome'),
	url(r'^orders', views.ceoorder,name='ceoorders'),
	url(r'^orders/pending', views.ceoorder,name='ceoorders'),
	url(r'^orders/past', views.ceoorderpast,name='ceoorderspast'),
	url(r'^user', views.ceouser,name='ceouser'),
	url(r'^products', views.ceoproducts,name='ceoproducts'),
	url(r'^feedback', views.ceoorder,name='ceofeedback'),
	url(r'^shipper_info', views.ceoorder,name='ceoshipper'),
	url(r'^login$', views.login,name='ceologin'),
	url(r'^logout/$', views.logout,name='ceologout'),
]
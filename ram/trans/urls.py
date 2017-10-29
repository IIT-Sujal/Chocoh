from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
	url(r'^payment/(?P<username>[\w.@+-]+)/$',views.payment,name='payment'),
	#url(r'^payment/$', views.payhome, name='payhome'),
	url(r'^payu-success/$', views.payu_success, name='payu_success'),
    url(r'^payu-failure$', views.payu_failure, name='payu_failure'),
    url(r'^payu-cancel$', views.payu_cancel, name='payu_cancel'),
]
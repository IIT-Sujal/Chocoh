from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^home', views.ceoorder,name='ceohome'),
	url(r'^orders', views.ceoorder,name='ceoorders'),
	url(r'^orders/pending', views.ceoorder,name='ceoorders'),
	url(r'^orders/past', views.ceoorderpast,name='ceoorderspast'),
	url(r'^delete_from_product/(?P<pk>[0-9]+)$', views.delete_from_product,name='delete_from_product'),
	url(r'^add_to_products', views.add_to_products,name='add_to_products'),
	url(r'^user', views.ceouser,name='ceouser'),
	url(r'^products', views.ceoproducts,name='ceoproducts'),
	url(r'^feedback', views.ceofeedback,name='ceofeedback'),
	url(r'^shipper_info', views.ceoorder,name='ceoshipper'),
	url(r'^login$', views.login,name='ceologin'),
	url(r'^logout/$', views.logout,name='ceologout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
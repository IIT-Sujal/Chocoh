from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from core import views as core_views


urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
]
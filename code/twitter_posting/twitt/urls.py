from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^login/?$', views.twitter_login),
	url(r'^logout/?$', views.twitter_logout),
	url(r'^login/authenticated/?$', views.twitter_authenticated),
    url(r'^', views.index),
]
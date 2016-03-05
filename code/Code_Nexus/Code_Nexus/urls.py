from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^facebook/', include('facebook_upload.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
]
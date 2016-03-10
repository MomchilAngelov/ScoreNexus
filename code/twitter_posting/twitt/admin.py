from django.contrib import admin

from .models import TwitterPost, User

admin.site.register(TwitterPost)
admin.site.register(User)
# Register your models here.

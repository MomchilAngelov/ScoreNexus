from django.db import models
from django.conf import settings
import os
import oauth2 as oauth
import requests
from twython import Twython
import re

class User(models.Model):
	Token_Auth = models.CharField(max_length=255)
	Token_Auth_Secret = models.CharField(max_length=255)

class TwitterPost(models.Model):
	text = models.CharField(max_length=255)
	link = models.CharField(max_length=255)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __unicode__(self):
		return u'%s' % self.text

	def get_absolute_url(self):
		return self.link

	# the following method is optional
	def get_twitter_message(self):
		return u'%s - %s' % (self.text, self.link)


TWITTER_MAXLENGTH = getattr(settings, 'TWITTER_MAXLENGTH', 140)

def post_to_twitter(sender, instance, *args, **kwargs):
	APP_KEY = "vzbqdzbtpCKoa5dbHw1JGwv2i"
	APP_SECRET = "Uc3Fi50PPb7f2j2JWO90VqQF5pocfuBiPzppl5E4Y5AaqLteNQ"

	twitter = Twython(APP_KEY, APP_SECRET, instance.user.Token_Auth, instance.user.Token_Auth_Secret)

	twitter.update_status(status=instance.get_twitter_message())

models.signals.post_save.connect(post_to_twitter, sender=TwitterPost)

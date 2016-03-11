from django.shortcuts import render
from django.http import HttpResponse
import re

import oauth2 as oauth
import cgi

# Django
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Project
from twitt.models import User
 
consumer = oauth.Consumer(settings.TWITTER_TOKEN, settings.TWITTER_SECRET)
client = oauth.Client(consumer)
request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authenticate_url = 'https://api.twitter.com/oauth/authenticate'

_global = []

def index(request):
	return render(request, 'twitt/index.html')

def twitter_login(request):
	# Step 1. Get a request token from Twitter.
	resp, content = client.request(request_token_url, "GET")
	if resp['status'] != '200':
		raise Exception("Invalid response from Twitter.")
	m = re.search(r"(?<==)(.*?)(?=&)", content.decode('ascii'))
	auth_token = m.group(0)
	# Step 2. Store the request token in a session for later use.
	request.session['request_token'] = dict(cgi.parse_qsl(content.decode('ascii')))
	global _global
	_global = dict(cgi.parse_qsl(content.decode('ascii')))

	# Step 3. Redirect the user to the authentication URL.
	url = "%s?oauth_token=%s" % (authenticate_url, auth_token)
	return HttpResponseRedirect(url)


@login_required
def twitter_logout(request):
    # Log a user out using Django's logout function and redirect them
    # back to the homepage.
    logout(request)
    return HttpResponseRedirect('/')

def twitter_authenticated(request):
	global _global 
	allData = _global
	# Step 1. Use the request token in the session to build a new client.
	token = oauth.Token(allData['oauth_token'], allData['oauth_token_secret'])
	token.set_verifier(request.GET['oauth_verifier'])
	client = oauth.Client(consumer, token)

	# Step 2. Request the authorized access token from Twitter.
	resp, content = client.request(access_token_url, "GET")
	if resp['status'] != '200':
		raise Exception("Invalid response from Twitter.")

	access_token = dict(cgi.parse_qsl(content))
	
	# Step 3. Lookup the user or create them if they don't exist.
		# When creating the user I just use their screen_name@twitter.com
		# for their email and the oauth_token_secret for their password.
		# These two things will likely never be used. Alternatively, you 
		# can prompt them for their email here. Either way, the password 
		# should never be used.

		# Save our permanent token and secret for later.
	user = User()
	user.Token_Auth = access_token[b'oauth_token'].decode('ascii')
	user.Token_Auth_Secret = access_token[b'oauth_token_secret'].decode('ascii')
	user.save()

	# Authenticate the user and log them in using Django's pre-built 
	# functions for these things.

	return HttpResponseRedirect('/')
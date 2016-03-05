from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a test app, using facebook GRAPH API with Django. This app should only be used by few people.We will not use any of the information you throw at us.")
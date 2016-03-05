from django.shortcuts import render


def index(request):
    return render(request, 'facebook_upload/index.html')
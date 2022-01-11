from django.shortcuts import render
from django.http import HttpResponse
from .models import djangoClasses


# simple http request > response to ensure page is functioning

def home(request):
    return HttpResponse('Hello World')

# Create your views here.

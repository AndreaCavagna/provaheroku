from django.shortcuts import render
from django.http import HttpResponse
import requests
import os


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')

    return render(request, '<h1>' + 'helloworld' + '</h1>')
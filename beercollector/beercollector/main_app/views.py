from django.shortcuts import render
from .models import *


# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>HELLO THERE</h1>')

def about(request):
    return render(request, 'about.html')

def beer_index(request):
    return render(request, 'beercollection/index.html', {'allbeers': beers_in_collection})
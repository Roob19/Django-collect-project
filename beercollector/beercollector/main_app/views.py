from django.shortcuts import render
from .models import The_beer


# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>HELLO THERE</h1>')

def about(request):
    return render(request, 'about.html')

def beer_index(request):
    return render(request, 'beercollection/index.html', {'allbeers': beers_in_collection})

def beer_details(request, beer_id):
    beer = The_beer.objects.get(id=beer_id)
    return render(request, 'beercollection/details.html', {'beer':beer})
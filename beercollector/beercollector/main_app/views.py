from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import The_beer

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse('<h1>HELLO THERE</h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def beer_index(request):
    all_beers = The_beer.objects.all()
    return render(request, 'beercollection/index.html', {'all_beers': all_beers})

def beer_details(request, beer_id):
    beer = The_beer.objects.get(id=beer_id)
    print('beer_details' , beer.id)
    # import pdb; pdb.set_trace()
    return render(request, 'beercollection/details.html', {'beer':beer})

class BeerCreate(CreateView):
    model = The_beer
    fields = '__all__'
    def get_success_url(self, **kwargs):
        return reverse('details', args=(self.object.id,))

class BeerUpdate(UpdateView):
    model = The_beer
    fields = ['name', 'style', 'abv', 'url_site']
    def get_success_url(self, **kwargs):
        return reverse('details', args=(self.object.id,))

class BeerDelete(DeleteView):
    model = The_beer
    success_url = '/allbeers/'
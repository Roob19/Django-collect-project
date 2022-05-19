from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import TheBeer, Hop
from .forms import BeerSamplingForm

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse('<h1>HELLO THERE</h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def beer_index(request):
    all_beers = TheBeer.objects.all()
    return render(request, 'beercollection/index.html', {'all_beers': all_beers})

def beer_details(request, beer_id):
    beer = TheBeer.objects.get(id=beer_id)
    # print('beer_details' , beer.id)
    # import pdb; pdb.set_trace()
    hops_beer_doesnt_have = Hop.objects.exclude(id__in = beer.hops.all().values_list('id'))
    beersampling_form = BeerSamplingForm()
    return render(request, 'beercollection/details.html', {'beer':beer, 'beersampling_form': beersampling_form, 'hops': hops_beer_doesnt_have})

def add_beersampling(request, beer_id):
    form = BeerSamplingForm(request.POST)
    if form.is_valid():
        new_beersampling = form.save(commit=False)
        new_beersampling.beer_id = beer_id
        new_beersampling.save()
    return redirect('details', beer_id=beer_id)

def assoc_hop(request, beer_id, hop_id):
    TheBeer.objects.get(id=beer_id).hops.add(hop_id)
    return redirect('details', beer_id=beer_id)

class BeerCreate(CreateView):
    model = TheBeer
    fields = ['brewery', 'name', 'style', 'abv', 'url_site']
    def get_success_url(self, **kwargs):
        return reverse('details', args=(self.object.id,))

class BeerUpdate(UpdateView):
    model = TheBeer
    fields = ['name', 'style', 'abv', 'url_site']
    def get_success_url(self, **kwargs):
        return reverse('details', args=(self.object.id,))

class BeerDelete(DeleteView):
    model = TheBeer
    success_url = '/allbeers/'
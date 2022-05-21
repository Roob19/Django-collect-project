import os
import boto3
import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import TheBeer, Hop, Photo
from .forms import BeerSamplingForm

# Create your views here.

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

def add_photo(request, beer_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, beer_id=beer_id)
        except:
            print('An error occured uploading file to S3')
    return redirect('details', beer_id=beer_id)

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
    # def get_success_url(self, **kwargs):
    #     return reverse('details', args=(self.object.id,))
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BeerUpdate(UpdateView):
    model = TheBeer
    fields = ['name', 'style', 'abv', 'url_site']
    def get_success_url(self, **kwargs):
        return reverse('details', args=(self.object.id,))

class BeerDelete(DeleteView):
    model = TheBeer
    success_url = '/allbeers/'
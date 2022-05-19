from django.contrib import admin
from .models import TheBeer, BeerSampling, Hop

# Register your models here.
admin.site.register(TheBeer)
admin.site.register(BeerSampling)
admin.site.register(Hop)

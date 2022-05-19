from django.db import models
from django.urls import reverse

DRINKS = (
    ('Morning', 'Morning'),
    ('Noon', 'Noon'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening'),
    ('Latenight', 'Latenight'),
    ('Madrugada', 'Madrugada')
)

class Hop(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('hops_detail', kwargs={'pk':self.id})

    def __str__(self):
        return self.name

# Create your models here.
# class TheBeer:
#     def __init__(self, brewery, name, style, abv, url_site):
#         self.brewery = brewery
#         self.name = name
#         self.style = style
#         self.abv = abv
#         self.url_site = url_site

class TheBeer(models.Model):
    brewery = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    abv = models.DecimalField(max_digits=3, decimal_places=1)
    url_site = models.CharField(max_length=254, blank=True)
    hops = models.ManyToManyField(Hop)

    def __str__(self):
        return self.name

# beers_in_collection = [
#     TheBeer('Russian River Brew Co', 'Pliny the Elder', 'Double IPA', 8.0, 'https://www.russianriverbrewing.com/pliny-the-elder/'),
#     TheBeer('Firestone Walker', 'Velvet Mirken', 'Oatmeal Stout aged in Bourbon Barrels', 8.5, 'https://www.firestonebeer.com/velvet-merkin-3-pack/'),
#     TheBeer('Moonraker Brewing Co', 'Thunder Cabbage', 'New England Triple IPA', 10.0, 'https://taplist.io/taplist-198630'),
# ]

class Photo(models.Model):
    url = models.CharField(max_length=200)
    beer = models.ForeignKey(TheBeer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo fro beer_id: {self.beer_id} @{self.url}"

class BeerSampling(models.Model):
    date = models.DateField('Date Sampled')
    drink = models.CharField(
        max_length=25, 
        choices=DRINKS, 
        default=DRINKS[0][0]
        )

    def __str__(self):
        return f"{self.get_drink_display()} on {self.date}"

    beer = models.ForeignKey(TheBeer, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

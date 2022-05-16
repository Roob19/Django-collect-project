from django.db import models

# Create your models here.
# class The_beer:
#     def __init__(self, brewery, name, style, abv, url_site):
#         self.brewery = brewery
#         self.name = name
#         self.style = style
#         self.abv = abv
#         self.url_site = url_site

class The_beer(models.Model):
    brewery = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    abv = models.DecimalField(max_digits=3, decimal_places=1)
    url_site = models.CharField(max_length=254)

    def __str__(self):
        return self.name

# beers_in_collection = [
#     The_beer('Russian River Brew Co', 'Pliny the Elder', 'Double IPA', 8.0, 'https://www.russianriverbrewing.com/pliny-the-elder/'),
#     The_beer('Firestone Walker', 'Velvet Mirken', 'Oatmeal Stout aged in Bourbon Barrels', 8.5, 'https://www.firestonebeer.com/velvet-merkin-3-pack/'),
#     The_beer('Moonraker Brewing Co', 'Thunder Cabbage', 'New England Triple IPA', 10.0, 'https://taplist.io/taplist-198630'),
# ]
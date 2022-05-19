from django.forms import ModelForm
from .models import BeerSampling

class BeerSamplingForm(ModelForm):
    class Meta:
        model = BeerSampling
        fields = ['date', 'weekday']
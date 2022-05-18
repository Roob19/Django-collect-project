from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('allbeers/', views.beer_index, name='index'),
    path('allbeers/<int:beer_id>', views.beer_details, name='details'),
    path('allbeers/create/', views.BeerCreate.as_view(), name='beer_create'),
    path('allbeers/<int:pk>/update/', views.BeerUpdate.as_view(), name='beer_update'),
    path('allbeers/<int:pk>/delete/', views.BeerDelete.as_view(), name='beer_delete'),
]
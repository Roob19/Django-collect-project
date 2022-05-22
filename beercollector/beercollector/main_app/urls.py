from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('allbeers/', views.beer_index, name='index'),
    path('allbeers/', views.user_index, name='mybeers'),
    path('allbeers/<int:beer_id>', views.beer_details, name='details'),
    path('allbeers/create/', views.BeerCreate.as_view(), name='beer_create'),
    path('allbeers/<int:pk>/update/', views.BeerUpdate.as_view(), name='beer_update'),
    path('allbeers/<int:pk>/delete/', views.BeerDelete.as_view(), name='beer_delete'),
    path('allbeers/<int:beer_id>/add_photo/', views.add_photo, name='add_photo'),
    path('allbeers/<int:beer_id>/add_beersampling/', views.add_beersampling, name='add_beersampling'),
    path('allbeers/<int:beer_id>/assoc_hop/<int:hop_id>', views.assoc_hop, name='assoc_hop'),
    path('accounts/signup/', views.signup, name='signup'),
]
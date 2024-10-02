from django.urls import path
from .views import KittenRatingListView, KittenRatingCreateView

urlpatterns = [
    path('kittens/<int:kitten_id>/ratings/', KittenRatingListView.as_view(), name='kitten-ratings'),
    path('kittens/rate/', KittenRatingCreateView.as_view(), name='kitten-rate'),
]
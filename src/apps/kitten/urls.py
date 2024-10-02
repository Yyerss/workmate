from django.urls import path
from .views import (
    KittenListView, KittenDetailView, KittenCreateView,
    KittenUpdateView, KittenDeleteView, BreedListView
)

urlpatterns = [
    path('breeds/', BreedListView.as_view(), name='breed-list'),
    path('kittens/', KittenListView.as_view(), name='kitten-list'),
    path('kittens/<int:pk>/', KittenDetailView.as_view(), name='kitten-detail'),
    path('kittens/add/', KittenCreateView.as_view(), name='kitten-add'),
    path('kittens/<int:pk>/edit/', KittenUpdateView.as_view(), name='kitten-edit'),
    path('kittens/<int:pk>/delete/', KittenDeleteView.as_view(), name='kitten-delete'),
]
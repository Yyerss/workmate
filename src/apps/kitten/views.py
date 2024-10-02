from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from .models import Kitten, Breed
from .serializers import KittenSerializer, KittenWriteSerializer, BreedSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from rest_framework import filters


# Create your views here.
class BreedListView(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittenListView(generics.ListAPIView):
    queryset = Kitten.objects.select_related('breed').prefetch_related('ratings').all()
    serializer_class = KittenSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['breed__name']


class KittenDetailView(generics.RetrieveAPIView):
    queryset = Kitten.objects.select_related('breed', 'owner').prefetch_related('ratings').all()
    serializer_class = KittenSerializer


class KittenCreateView(generics.CreateAPIView):
    serializer_class = KittenWriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class KittenUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenWriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if self.get_object().owner == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied('You do not have permission to edit this kitten.')


class KittenDeleteView(generics.DestroyAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenWriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.owner == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied('You do not have permission to delete this kitten.')

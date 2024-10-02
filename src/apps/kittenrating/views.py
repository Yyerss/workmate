from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied, ValidationError
from .models import KittenRating
from .serializers import KittenRatingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from rest_framework import filters


class KittenRatingCreateView(generics.CreateAPIView):
    serializer_class = KittenRatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        kitten = serializer.validated_data.get('kitten')
        if KittenRating.objects.filter(kitten=kitten, user=self.request.user).exists():
            raise ValidationError('You have already rated this kitten.')
        serializer.save(user=self.request.user)


class KittenRatingListView(generics.ListAPIView):
    serializer_class = KittenRatingSerializer

    def get_queryset(self):
        kitten_id = self.kwargs.get('kitten_id')
        return KittenRating.objects.filter(kitten__id=kitten_id)

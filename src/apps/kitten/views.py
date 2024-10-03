from .models import Kitten, Breed
from .serializers import KittenSerializer, KittenWriteSerializer, BreedSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import filters
from .mixins import KittenQuerysetMixin, OwnerPermissionMixin


# Create your views here.
class BreedListView(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittenListView(KittenQuerysetMixin, generics.ListAPIView):
    serializer_class = KittenSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['breed__name']


class KittenDetailView(KittenQuerysetMixin, generics.RetrieveAPIView):
    serializer_class = KittenSerializer


class KittenCreateView(generics.CreateAPIView):
    serializer_class = KittenWriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class KittenUpdateView(KittenQuerysetMixin, OwnerPermissionMixin, generics.RetrieveUpdateAPIView):
    serializer_class = KittenWriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = self.get_object()
        self.check_owner_permission(instance)
        serializer.save()


class KittenDeleteView(KittenQuerysetMixin, OwnerPermissionMixin, generics.DestroyAPIView):
    serializer_class = KittenWriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        self.check_owner_permission(instance)
        instance.delete()

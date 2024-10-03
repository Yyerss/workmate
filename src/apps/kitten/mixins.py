from .models import Kitten
from rest_framework.exceptions import PermissionDenied


class KittenQuerysetMixin:
    def get_queryset(self):
        return Kitten.objects.select_related('breed', 'owner').prefetch_related('ratings')


class OwnerPermissionMixin:
    def check_owner_permission(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied('You do not have permission to perform this action.')
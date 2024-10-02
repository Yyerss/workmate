from django.db import models
from ..kitten.models import Kitten
from ..custom_auth.models import CustomUser


# Create your models here.
class KittenRating(models.Model):
    kitten = models.ForeignKey(Kitten, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['kitten', 'user']

    def __str__(self):
        return f'{self.user} rated {self.kitten} with {self.rating}'

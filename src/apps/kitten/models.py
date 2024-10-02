from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Breed(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Kitten(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='kittens')
    color = models.CharField(max_length=50)
    age_in_months = models.PositiveIntegerField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kittens')

    def __str__(self):
        return f'{self.color} kitten, {self.age_in_months} months old'

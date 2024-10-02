import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from ..kitten.models import Kitten, Breed
from .models import KittenRating
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(email='testuser@example.com', password='testpassword')


@pytest.fixture
def breed(db):
    return Breed.objects.create(name="Siamese")


@pytest.fixture
def kitten(db, breed, user):
    return Kitten.objects.create(breed=breed, color="Black", age_in_months=6, description="Cute kitten", owner=user)


@pytest.mark.django_db
def test_kitten_rating(api_client, user, kitten):
    api_client.force_authenticate(user=user)
    url = reverse('kitten-rate')
    data = {'kitten': kitten.id, 'rating': 5}
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert KittenRating.objects.filter(kitten=kitten, user=user).exists()

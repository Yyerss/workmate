import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Kitten, Breed


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def breed(db):
    return Breed.objects.create(name="Siamese")


@pytest.fixture
def kitten(db, breed):
    return Kitten.objects.create(breed=breed, color="Black", age_in_months=6, description="Cute kitten")


@pytest.mark.django_db
def test_kitten_list(api_client, kitten):
    url = reverse('kitten-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) > 0

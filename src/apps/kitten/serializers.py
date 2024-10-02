from rest_framework import serializers
from .models import Breed, Kitten
from django.db.models import Avg


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name']


class KittenWriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Kitten
        fields = ['id', 'breed', 'color', 'age_in_months', 'description', 'owner']


class KittenSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    breed = BreedSerializer()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Kitten
        fields = ['id', 'breed', 'color', 'age_in_months', 'description', 'owner', 'average_rating']

    def get_average_rating(self, obj):
        average = obj.ratings.aggregate(Avg('rating'))['rating__avg']
        return round(average, 2) if average is not None else None
from rest_framework import serializers
from .models import KittenRating

class KittenRatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = KittenRating
        fields = ['id', 'kitten', 'user', 'rating']
        extra_kwargs = {
            'rating': {'min_value': 1, 'max_value': 5}  # Оценка от 1 до 5
        }
from rest_framework import serializers
from .models import Food, Meal

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer which maps the Model instance to JSON format."""

    class Meta:
      """Meta class to map serializer's fields with model's fields."""
      model = Food
      fields = ('id', 'name', 'calories')

class MealSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer which maps the Model instance to JSON format."""
    foods = FoodSerializer(many=True)

    class Meta:
      """Meta class to map serializer's fields with model's fields."""
      model = Meal
      fields = ('id', 'name', 'foods')
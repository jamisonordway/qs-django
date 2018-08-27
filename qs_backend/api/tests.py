from api.models import Food
from django.test import TestCase
import json
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase

class ModelTestCase(TestCase):
    """Defines test suite for the food model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.food_name = "Elote"
        self.food_calories = 300
        self.food = Food(name=self.food_name, calories=self.food_calories)
    
    def test_model_can_create_a_food(self):
        """Test the food model can create a food."""
        count = Food.objects.count()
        self.food.save()
        new_count = Food.objects.count()
        self.assertNotEqual(count, new_count)

# Create your tests here.

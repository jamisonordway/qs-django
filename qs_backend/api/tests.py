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

class FoodViewsTest(TestCase):
    """Defines test suite for the food api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.taco = Food.objects.create(name="taco", calories=400)
        self.salad = Food.objects.create(name="salad", calories=200)
        self.steak = Food.objects.create(name="steak", calories=700)

    def test_status_for_all_foods(self):
        response = self.client.get('api/vi/foods')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_all_foods(self):
        response = self.client.get('/api/v1/foods')
        js_res = self.client.get('/api/v1/foods').json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(js_res[0]["name"], self.taco.name)
        self.assertEqual(js_res[0]["calories"], self.taco.calories)
        self.assertEqual(js_res[2]["name"], self.steak.name)
        self.assertEqual(js_res[2]["calories"], self.steak.calories)

    def test_get_a_single_food(self):
        food = Food.objects.first()
        response = self.client.get(f'/api/v1/foods/{food.id}')
        js_res = response.json()
        self.assertEqual(js_res["name"], self.taco.name)
    
    def test_create_a_food(self):
        response = self.client.post('/api/v1/foods/', {'food': {'name': 'pozole', 'calories': 500}}, format='json')
        js_res = response.json()
        self.assertEqual(js_res["name"], "pozole")
        self.assertEqual(js_res["calories"], 500)

    def test_update_food(self):
        food = Food.objects.first()
        change = {"food": {"name": "quesadilla", "calories": 200}}
        response = self.client.patch(f"/api/v1/foods/{food.id}", change, format="json")
        js_res = response.json()
        self.assertEqual(js_res["name"], "quesadilla")
        self.assertEqual(js_res["calories"], 200)

    def test_delete_food(self):
        food = Food.objects.first()
        response = self.client.delete(f"/api/v1/foods/{food.id}")
        self.assertEqual(response.satus_code, status.HTTP_204_NO_CONTENT)
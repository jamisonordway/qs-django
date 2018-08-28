import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from api.serializers import FoodSerializer, MealSerializer
from rest_framework import viewsets
from rest_framework import Response
from api.models import Food, Meal

class FoodViews(viewsets.ViewSet):

    def list(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, food_id=None):
        foods = Food.objects.all()
        food = get_object_or_404(foods, id=food_id)
        serializer = FoodSerializer(food)
        return Response(serializer.data)
    
    def create(self, request):
        food_attributes = json.loads(request.body)["food"]
        food = Food(name=food_attributes["name"], calories=food_attributes["calories"])
        food.save()

        serializer = FoodSerializer(food)
        return Response(serializer.data)

    def update(self, request, food_id=None):
        foods = Food.objects.all()
        food = get_object_or_404(foods, id=food_id)
        food_attributes = json.loads(requst.body)["food"]
        food.name = food_attributes["name"]
        food.calories = food_attributes["calories"]
        food.save()
        serializer = FoodSerializer(food)
        return Response(serializer.data)
    
    def destroy(self, request, food_id=None):
        foods = Food.objects.all()
        food = get_object_or_404(foods, id=food_id)
        food.delete()
        return HttpResponse(status=204)

class MealViews(viewsets.ViewSet):
      
      def list(self, request):
          meals = Meal.objects.all()
          serializer = MealSerializer(meals, many=True)
          return Response(serializer.data)
      
      def retrieve(self, request, meal_id=None):
          meals = Meal.objects.all()
          meal = get_object_or_404(meals, id=meal_id)
          serializer = MealSerializer(meal)
          return Response(serializer.data)
      
      def create(self, request, meal_id=None, food_id=None):
          meal = get_object_or_404(Meal, id=meal_id)
          food = get_object_or_404(Food, id=food_id)
          meal.foods.add(food)
          message = { "message": f"Successfully added {food.name} to {meal.name}" }
          return Response(message, status=201)

      def destroy(self, request, meal_id=None, food_id=None):
          meal = get_object_or_404(Meal, id=meal_id)
          food = get_object_or_404(Food, id=food_id)
          meal.foods.remove(food)
          message = { "message": f"Successfully removed {food.name} from {meal.name}" }
          return Response(message, status=204)
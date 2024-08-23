# src/recipes/views.py
from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.published()
    serializer_class = RecipeSerializer

class RecipeCreateView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

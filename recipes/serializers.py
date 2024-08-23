# src/recipes/serializers.py
from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients', 'instructions', 'is_published']
        read_only_fields = ['is_published']  # Only admin can set the publication status
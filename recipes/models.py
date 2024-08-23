# src/recipes/models.py
from django.db import models

class RecipeQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RecipeQuerySet.as_manager()

    def __str__(self):
        return self.title
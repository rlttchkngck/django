from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'ingredients', 'instructions', 'created_at', 'updated_at', 'is_published')
    search_fields = ('title', 'ingredients', 'instructions', 'is_published')
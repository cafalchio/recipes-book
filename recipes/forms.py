from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'cooking_time', 'servings', 
                'ingredients', 'instructions', 'image', 'is_public', 'user')
        
    
from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('user',)
        fields = ('title', 'description', 'cooking_time', 'servings',
                  'ingredients', 'instructions', 'is_public', 'image')

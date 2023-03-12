from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'cooking_time', 'servings', 
                'ingredients', 'instructions', 'image', 'is_public')
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'cooking_time': forms.TextInput(attrs={'class': 'form-control'}),
        #     'servings': forms.TextInput(attrs={'class': 'form-control'}),
        #     'ingredients': forms.Textarea(attrs={'class': 'form-control'}),
        #     'instructions': forms.Textarea(attrs={'class': 'form-control'}),
        #     'image': forms.URLInput(attrs={'class': 'form-control'}),
        #     'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        # }
    
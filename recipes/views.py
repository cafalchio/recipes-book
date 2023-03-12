from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from recipes.models import Recipe

def get_all(request):
    recipes = Recipe.objects.filter(is_public=True)
    print(recipes)
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

def get(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if recipe.is_public:
        return render(request, 'recipe.html', {'recipe': recipe})
    else:
        return HttpResponseForbidden()  
    
@login_required
def get_my_recipes(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes.html', {'recipes': recipes})

@login_required
def get_my_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if recipe.user == request.user:
        return render(request, 'recipe.html', {'recipe': recipe})
    else:
        return HttpResponseForbidden()

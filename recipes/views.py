from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from recipes.models import Recipe

def public_recipes(request):
    recipes = Recipe.objects.filter(is_public=True)
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

# def public_recipe(request, recipe_id):
#     recipe = Recipe.objects.get(id=recipe_id)
#     if recipe.is_public:
#         return render(request, 'recipes/recipe.html', {'recipe': recipe})
#     else:
#         return HttpResponseForbidden()

# @login_required
# def get_my_recipes(request):
#     recipes = Recipe.objects.filter(user=request.user)
#     return render(request, 'recipes.html', {'recipes': recipes})

# @login_required
# def get_my_recipe(request, recipe_id):
#     recipe = Recipe.objects.get(id=recipe_id)
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, request.FILES, instance=recipe)
#         if form.is_valid():
#             form.save()
#             return render(request, 'recipe.html', {'recipe': recipe})    
#         return render(request, 'recipe.html', {'recipe': recipe})
    
#     elif request.method == 'GET':
#         if recipe.user == request.user:
#             return render(request, 'recipe.html', {'recipe': recipe})
#         else:
#             return HttpResponseForbidden()    
        
#     elif request.method == 'DELETE':
#         pass

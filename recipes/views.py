from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from recipes.forms import RecipeForm
from recipes.models import Recipe

def public_recipes(request):
    """List all public recipes"""
    recipes = Recipe.objects.filter(is_public=True)
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

def public_recipe(request, recipe_id):
    """Render selected public recipe detailed view page"""
    recipe = get_object_or_404(Recipe, pk=recipe_id, is_public=True)
    context = {
        'recipe': recipe,
    }
    return render(request, 'recipes/recipe.html', context)

@login_required
def get_my_recipes(request):
    """List all recipes for the authenticated user"""
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

@login_required
def get_my_recipe(request, recipe_id):
    """Render detailed view for a specific recipe of the authenticated user"""
    recipe = get_object_or_404(Recipe, user=request.user, id=recipe_id)
    return render(request, 'recipes/recipe.html', {'recipe': recipe})

@login_required
def add_recipe(request):
    """Add a new recipe for the authenticated user"""
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('my_recipes')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})
        
@login_required     
def delete_recipe(request, recipe_id):
    """Delete a recipe for the authenticated user"""
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    recipe.delete()
    return redirect('my_recipes')

@login_required    
def edit_recipe(request, recipe_id):
    """Edit a recipe for the authenticated user"""
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('my_recipes')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/edit_recipe.html', {'form': form})
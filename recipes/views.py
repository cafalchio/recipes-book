from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from recipes.forms import RecipeForm
from recipes.models import Recipe


# Error handlers
def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)

def error_403_view(request, exception):
    return render(request, '403.html', status=403)

def error_400_view(request, exception):
    return render(request, '400.html', status=400)

# index
def index(request):
    return render(request, 'index.html')

# Recipes views
def public_recipes(request):
    """List all public recipes"""
    recipes = Recipe.objects.filter(is_public=True)
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

def get_my_recipe(request, recipe_id):
    """Render selected recipe detailed view page"""
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.is_public or request.user == recipe.user:
        context = {
            'recipe': recipe,
        }
        return render(request, 'recipes/recipe.html', context)
    else:
        return HttpResponseForbidden()

@login_required
def get_my_recipes(request):
    """List all recipes for the authenticated user"""
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

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
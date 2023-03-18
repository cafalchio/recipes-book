from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from recipes.forms import RecipeForm
from recipes.models import Recipe

def public_recipes(request):
    recipes = Recipe.objects.filter(is_public=True)
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

def public_recipe(request, recipe_id):
    """
    Render selected public recipe detailed view page
    """
    recipe = get_object_or_404(Recipe, pk=recipe_id, is_public=True)
    context = {
        'recipe': recipe,
    }
    return render(request, 'recipes/recipe.html', context)

@login_required
def get_my_recipes(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

@login_required
def get_my_recipe(request, recipe_id):
    recipe = Recipe.objects.filter(user=request.user , id=recipe_id)
    return render(request, 'recipes/recipe.html', {'recipe': recipe})

@login_required
# tutorial from https://www.youtube.com/watch?v=CVEKe39VFu8 
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('my_recipes')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})
        
@login_required     
def delete_recipe(request, recipe_id):
    print(f"REQUEST USER: {request.user}")
    print(f"RECIPE USER: {recipe_id.user}")
    if request.user != recipe_id.user:
        return redirect('my_recipes')
    recipe_id.delete()

@login_required    
def edit_recipe(request, recipe_id):
    if request.user != recipe_id.user:
        return redirect('my_recipes')

        
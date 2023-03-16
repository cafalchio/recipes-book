from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from recipes.forms import RecipeForm
from recipes.models import Recipe

def public_recipes(request):
    recipes = Recipe.objects.filter(is_public=True)
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

def public_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if recipe.is_public:
        return render(request, 'recipes/recipe.html', {'recipe': recipe})
    else:
        return HttpResponseForbidden()

@login_required
def get_my_recipes(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

@login_required
def get_my_recipe(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/recipe.html', {'recipes': recipes})

@login_required
def add_recipe(request):
    submited = False
    return render(request, 'recipes/add_recipe.html', {'form': RecipeForm()})
    # form = RecipeForm(request.POST or None, request.FILES or None)
    # if request.method == 'POST':
        
        
        
    
@login_required     
def delete_recipe(request, recipe_id):
    print(f"REQUEST USER: {request.user}")
    print(f"RECIPE USER: {recipe_id.user}")
    if request.user != recipe_id.user:
        return render('') # send to a page and show a message 
    recipe_id.delete()

def edit_recipe(request, recipe_id):
    if request.user != recipe_id.user:
        return render('') # send to a page and show a message 
    
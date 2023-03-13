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
    return render(request, 'recipes.html', {'recipes': recipes})

@login_required
def add_recipe(request, recipe_id):
    form = RecipeForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'recipe.html', {'recipe': recipe})    
        return # show error message in the form
    
@login_required     
def delete_recipe(request, recipe_id):
    if request.user != recipe_id.user:
        return render('') # send to a page and show a message 
    # delete

def edit_recipe(request, recipe_id):
    if request.uer != recipe_id.user:
        return render('') # send to a page and show a message 
    
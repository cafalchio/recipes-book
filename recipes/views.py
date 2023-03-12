from django.shortcuts import render
from models import Recipe
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from recipes.forms import RecipeForm
from django.shortcuts import redirect

class RecipeView(View):
    # all public recipes
    def get(self, request):
        recipes = Recipe.objects.filter(is_public=True)
        return render(request, 'recipes.html', {'recipes': recipes})
    
    def get(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        if recipe.is_public:
            return render(request, 'recipe.html', {'recipe': recipe})
        else:
            return HttpResponseForbidden()  
        
    @login_required
    def get(self, request):
        recipes = Recipe.objects.filter(user=request.user)
        return render(request, 'recipes.html', {'recipes': recipes})
    
    @login_required
    def get(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        if recipe.user == request.user:
            return render(request, 'recipe.html', {'recipe': recipe})
        else:
            return HttpResponseForbidden()
   
    @login_required
    def delete(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        if recipe.user == request.user:
            recipe.delete()
            return redirect('recipes')
        else:
            return HttpResponseForbidden()
    
    @login_required
    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipes')
        else:
            return render(request, 'new_recipe.html', {'form': form})
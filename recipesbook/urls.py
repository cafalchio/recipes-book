from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.shortcuts import render
from recipes import views as recipe_views
from web_page import views as web_page_views
from django.conf.urls import handler400, handler403, handler404, handler500


def handler400(request, exception):
    return render(request, '400.html', status=400)

def handler403(request, exception):
    return render(request, '403.html', status=403)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

urlpatterns = [
    path('', recipe_views.index , name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('recipes/', recipe_views.public_recipes, name='recipe_list'),
    path('my_recipes/', recipe_views.get_my_recipes, name='my_recipes'),
    path('recipes/recipe/<int:recipe_id>/', recipe_views.get_my_recipe, name='recipe_detail'),
    path('recipes/delete/<int:recipe_id>/', recipe_views.delete_recipe, name='delete_recipe'),
    path('public_recipe/<int:recipe_id>/', recipe_views.public_recipe, name='public_recipe'),
    path('recipes/add/', recipe_views.add_recipe, name='add_recipe'),
    path('recipes/edit/<int:recipe_id>/', recipe_views.edit_recipe, name='edit_recipe'),
]



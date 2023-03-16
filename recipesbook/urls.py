from django.contrib import admin
from django.urls import path, include
from recipes import views as recipe_views
from web_page import views as web_page_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', web_page_views.index , name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('recipes/', recipe_views.public_recipes, name='recipe_list'),
    path('my_recipes/', recipe_views.public_recipes, name='my_recipes'),
    path('recipes/delete/<int:recipe_id>/', recipe_views.delete_recipe, name='delete_recipe'),
    path('public_recipe/<int:recipe_id>/', recipe_views.public_recipe, name='public_recipe'),
    path('recipes/add/', recipe_views.add_recipe, name='add_recipe'),
]
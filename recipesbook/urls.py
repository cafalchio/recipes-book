"""recipesbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from recipes import views as recipe_views
from web_page import views as web_page_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_page/', web_page_views.login_page, name='login_page'),
    path('logout/', web_page_views.logout_view, name='logout'),
    path('', web_page_views.home , name='home'),
    path('recipes/', recipe_views.public_recipes, name='recipe_list'),
]

    # path('recipes/<int:recipe_id>/', RecipeView.as_view(), name='recipe_detail'),
    # path('my-recipes/', RecipeView.as_view(), name='my_recipe_list'),
    # path('my-recipes/<int:recipe_id>/', RecipeView.as_view(), name='my_recipe_detail'),
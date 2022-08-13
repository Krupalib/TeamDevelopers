from django.urls import path
from . import views


urlpatterns = [
    path('', views.recipe, name='dashboard-recipe'),
    path('staff/', views.staff, name='staff'),
    path('recipe/', views.recipe, name='recipe'),
    path('steps/<int:id>/', views.steps, name='steps'),
    path('rating/',views.rate_recipe, name='rate-view'),
    path('recipes_received/',views.recipes_received, name='recipe_received'),
    path('recipe/recipes_received/',views.recipes_received, name='recipe_received'),
]

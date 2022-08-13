from django.urls import path
from . import views


urlpatterns = [

#    path('staff/', views.staff, name='staff'),    EXAMPLE
path('add_recipe/', views.add_recipe, name='add_recipe'),
path('add_recipe/add_steps/<int:id>/', views.add_steps, name='add_steps'),
path('recipe/add_recipe', views.add_recipe, name='add_recipe'),


]

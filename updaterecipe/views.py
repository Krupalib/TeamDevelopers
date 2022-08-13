from django.shortcuts import render
from dashboard.models import Recipes,Utensils,Ingredients,process_steps,CATEGORY,keywords
# Create your views here.

def add_recipe(request):
    flag = False
    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')
        recipe_id = request.POST.get('recipe_id')
        cooking_time = request.POST.get("cooking_time")
        description = request.POST.get("description")
        number_of_serves = request.POST.get("number_of_serves")
        keyword = request.POST.get("keyword")
        rec = Recipes(recipe_name = recipe_name, recipe_id = recipe_id, cooking_time = cooking_time, number_of_serves= number_of_serves)
        rec.description = description
        all_recipes = Recipes.objects.all()

        for recipe in all_recipes:


            if (recipe.recipe_id == int(recipe_id)) :
                status = "Recipe ID already exists"
                print("You are in if statement")
                return render(request, 'updaterecipe/new_recipe.html', {'flag': flag, 'status': status})


        rec.save()
        k = keywords()
        k.recipe_id = Recipes.objects.get(recipe_id__icontains = rec.recipe_id)
        k.keyword = keyword
        k.save()
        flag = True
        status = "Recipe added Successfully"
        return render(request, 'updaterecipe/new_recipe.html',{'flag': flag, 'status' : status, 'rec' : rec})

    return render(request, 'updaterecipe/new_recipe.html')


def add_steps(request,id ):

    if request.method == "POST":
        step_no = request.POST.get("step_no")
        utensil = request.POST.get("utensil")
        ingredient = request.POST.get("ingredient")
        step_process = request.POST.get("process")
        temperature = request.POST.get("temperature")
        cooking_time = request.POST.get("cooking_time")


        process = process_steps()

        process.recipe_id = Recipes.objects.get(recipe_id__icontains = id)
        process.step_no = step_no
        process.utensil_id = Utensils.objects.get(utensil_name = utensil)
        process.ingredient_id = Ingredients.objects.get(ingredient_name = ingredient)
        process.temperature = temperature
        process.process = step_process
        process.time = cooking_time

        process.save()



    return render(request, 'updaterecipe/add_steps.html',{'utensils':list(Utensils.objects.all()), 'ingredients': Ingredients.objects.all(),'id' : id})

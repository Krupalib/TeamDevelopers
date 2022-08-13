from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from dashboard.models import Recipes, userRecipes, Utensils,Ingredients,keywords,process_steps,ratings,shared_recipes
from django.contrib.auth.decorators import login_required
from user.models import user_model
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request, 'dashboard/staff.html')

def recipe(request):
    recipe_list = Recipes.objects.all()
    recipe_dict = {'recipe' : recipe_list}
    Ingredients_list = Ingredients.objects.all()


    keyword_list = list()
    keyword_list_result = list()    #keyword_list =  list(dict.fromkeys(keyword_list))

    for inst in keywords.objects.all():
        flag = True
        for k in keyword_list_result:
            if inst.keyword == k.keyword:
                flag = False
        if flag == True:
            keyword_list_result.append(inst)
    print(keyword_list)
    result = list()
    name_of_recipe_flag = False
    cooking_time_flag = False
    if "name_of_recipe" in request.GET or "cooking_time" in request.GET:
        if "name_of_recipe" in request.GET:
            name_of_recipe = request.GET["name_of_recipe"]
            name_of_recipe_flag = True

        if  "cooking_time" in request.GET:
            cooking_time = request.GET["cooking_time"]
            cooking_time_flag = True

    if "name_of_recipe" in request.GET and "cooking_time" in request.GET:
            filtered_recipes_for_name_cooking_time = Recipes.objects.filter(recipe_name__icontains = name_of_recipe).filter(cooking_time__icontains = cooking_time)
    elif "name_of_recipe" in request.GET:
             filtered_recipes_for_name_cooking_time = Recipes.objects.filter(recipe_name__icontains = name_of_recipe)
    elif "cooking_time" in request.GET :
            filtered_recipes_for_name_cooking_time = Recipes.objects.filter(cooking_time__icontains = cooking_time)
    else:
            filtered_recipes_for_name_cooking_time = Recipes.objects.all()

###############3############################################################################################33
    name_of_ingredient_flag = False
    keyword_flag = False

    if "name_of_ingredient" in request.GET:
        name_of_ingredient_flag = True
        ingredient = request.GET["name_of_ingredient"]
        filtered_recipes_for_ingredient = list(process_steps.objects.filter(ingredient_id__ingredient_name__icontains = ingredient))
    if "keyword" in request.GET:
        keyword_flag = True
        keyword = request.GET["keyword"]
        filtered_recipes_for_keyword = list(keywords.objects.filter(keyword__icontains = keyword))


    if name_of_ingredient_flag and keyword_flag:
        for rec in filtered_recipes_for_name_cooking_time:
            for x in filtered_recipes_for_keyword:
                for y in filtered_recipes_for_ingredient:
                    if (rec.recipe_id == x.recipe_id.recipe_id == y.recipe_id.recipe_id):
                        result.append(rec)

    elif name_of_ingredient_flag:
        for rec in filtered_recipes_for_name_cooking_time:
            for x in filtered_recipes_for_ingredient:
                if (rec.recipe_id == x.recipe_id.recipe_id):
                    result.append(rec)

    elif keyword_flag:
        for rec in filtered_recipes_for_name_cooking_time:
            for x in filtered_recipes_for_keyword:
                if (rec.recipe_id == x.recipe_id.recipe_id):
                    result.append(rec)
    elif cooking_time_flag or name_of_recipe_flag:
        result = filtered_recipes_for_name_cooking_time
    else:
        result = recipe_list


    ratings_flag = False
    if "rating" in request.GET:

        ratings_flag = True
        rating = request.GET['rating']
        result_for_rating = list(ratings.objects.filter(rating__icontains = rating))

    final_result = list()
    if ratings_flag:
        #final_result= result_for_rating

         for r  in result:
            for x in result_for_rating:
                if(x.recipe_id != None):
                    if (r.recipe_id == x.recipe_id.recipe_id):
                        final_result.append(r)
    else:
        final_result = result
    final_result = list(dict.fromkeys(final_result))

    return render(request, 'dashboard/Recipe.html', {'recipe' : final_result, 'ingredient' : Ingredients_list, 'keyword' : keyword_list_result})

def process(request):
    webpage_list = process_steps.objects.order_by('step_no')
    date_dict = {'access_records' : webpage_list}


@login_required(login_url="/login/")
def steps(request,id):
    print(type(id))
    if request.method == "POST":
        if 'first' in request.POST:
            val = 1
        elif 'second' in request.POST:
            val = 2
        elif 'third' in request.POST:
            val = 3
        elif 'fourth' in request.POST:
            val = 4
        elif 'fifth' in request.POST:
            val = 5
        r = ratings()
        r.user_id = request.user
        r.recipe_id = Recipes.objects.get(recipe_id__icontains = id)
        r.rating = val
        rec = ratings.objects.filter(user_id__username__icontains = request.user)

        for rat in rec:
            if rat.recipe_id == Recipes.objects.get(recipe_id__icontains = id):
                rat.delete()
                #ratings.object.get(recipe_id__icontains = id,user_id__username__icontains = request.user ).delete()


        r.save()

    current_user = request.user
    #print(current_user)
    process = list()
    alldata = process_steps.objects.all()
    process = list(process_steps.objects.filter(recipe_id__recipe_id__icontains = id))
    n = len(process)
    for i in range(1,n):
        already_sorted = True
        for j in range(n - i - 1):
            if process[j].step_no > process[j + 1].step_no:
                    # If the item you're looking at is greater than its
                    # adjacent value, then swap them
                    process[j], process[j + 1] = process[j + 1], process[j]

                    # Since you had to swap two elements,
                    # set the `already_sorted` flag to `False` so the
                    # algorithm doesn't finish prematurely
                    already_sorted = False
            # If there were no swaps during the last iteration,
            # the array is already sorted, and you can terminate



    process = list()
    alldata = process_steps.objects.all()



    process_without_number_of_serving = list(process_steps.objects.filter(recipe_id__recipe_id__icontains = id))

    x = Recipes.objects.get(recipe_id = int(id) )

    if 'number_of_serves' in request.GET:
        n = request.GET['number_of_serves']

        for r in process_without_number_of_serving:


            r.Quantity =(( int(r.Quantity))/int(x.number_of_serves)*int(n))
            process.append(r)
            print(r.Quantity)
    else:
        for pro in process_without_number_of_serving:
            process.append(pro)



    #user_id = user.user_model.filter(user_id__icontains = )
    max_step = None
    for x in process:
        if max_step == None or x.step_no > max_step:
            max_step = x.step_no

        steps_list = list()
        if already_sorted:
            break
    process_dict = {'process' : process}
    user_list = User.objects.all()
    return render(request,'dashboard/steps.html', {'process' : process,'recipe' : x,'user':current_user,'user_list':user_list})


def rate_recipe(request):

    if request.method == "POST":
        print("you are in the rating url")
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        current_user = request.POST.get('current_user')
        #aprint(type(current_user))   # current_user is a string
        #print(type(el_id))    el_id is a string
        obj = ratings()
        user_id = request.user
    #    y = ratings.objects.filter(user_id__username__icontains = request.user)


        obj.create_ratings(val)
        obj.user_id = request.user
        obj.recipe_id = Recipes.objects.get(recipe_id = request.POST['el_id'])

        print(obj.recipe_id)

        # for ob in y:
        #     # print(type(ob.recipe_id))
        #     # print(type(el_id))
        #     if ob.recipe_id == el_id:
        #         ob.delete()

        obj.save()

        return JsonResponse({'success':'true', 'score': val}, safe=False)
    return JsonResponse({'success':'false'})

        ######################
@login_required(login_url="/login/")
def recipes_received(request):

    recipe_list = list()
    for data in shared_recipes.objects.all():
        if data.shared_to == request.user:
            recipe_list.append(data)


    return render(request, 'dashboard/recipes_received.html', {'recipe_list': recipe_list})

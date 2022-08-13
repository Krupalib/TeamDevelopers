from django.shortcuts import  render, redirect
from .forms import NewUserForm,EditProfileForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from user.models import user_model
from dashboard.models import Recipes,shared_recipes
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


def register(request):
	form = NewUserForm()
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			user_object = user_model()
			user_object.create_user_model(user.username, user.email)
			user_object.save()
			return redirect('user-login')
		messages.error(request, "Unsuccessful registration. Invalid information.")

	return render (request, "user/register.html", context={"register_form":form})

@login_required(login_url="/login/")
def UserEditView(request):


	# if request.method == "POST":
	# 	email_id = request.POST.get("email_id")

	if request.method == 'POST':

		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect( '/view_profile')
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form}
		return render(request, 'user/edit_profile.html', args)

	#
	# return render (request, "user/edit_profile.html")

@login_required(login_url="/login/")
def view_profile(request):

	  user = request.user
	  args = {'user': user}
	  return render(request, 'user/profile.html', args)

def share_recipe(request):
	if request.method == "POST":
		recipe = request.POST.get('recipe')
		shared_to = request.POST.get('shared_to')
		shared_by = request.user

		x= shared_recipes()
		x.recipe_id = Recipes.objects.get(recipe_id = int((recipe)))
		# for rec in Recipes.objects.all():
		# 	if rec.recipe_id == recipe:
		# 		x.recipe_id = rec
		x.shared_by = User.objects.get(username__icontains = shared_by)
		x.shared_to = User.objects.get(username__icontains = shared_to)
		x.save()


		return redirect('/recipe/')

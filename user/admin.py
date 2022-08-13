from django.contrib import admin
from .models import user_model
from django.contrib.auth.models import Group

# Register your models here.
class user_model_admin(admin.ModelAdmin):
    list_display = ('username','email')


admin.site.register(user_model, user_model_admin)

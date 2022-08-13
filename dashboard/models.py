from django.db import models
from django.contrib.auth.models import User
from user.models import user_model
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
CATEGORY = (
      ('Breakfast', 'Breakfast'),
      ('Lunch', 'Lunch'),
      ('Dinner', 'Dinner'),
)

unit_of_quantity = (('ml','ml'),('kg','kg'),('gram','gram'),('undefined','undefined'))

unit_of_temperature = (('°C','°C'),('°F','°F'),('undefined','undefined'))

unit_of_time = (('seconds','seconds'),('minutes','minutes'),('hours','hours'))



class Utensils(models.Model):
    utensil_name = models.CharField(max_length = 100, null=True)
    utensil_id = models.PositiveIntegerField(null=True)
    def  __str__(self):
        return f'{self.utensil_id}-{self.utensil_name}'


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length = 100, null=True)
    ingredient_id = models.PositiveIntegerField(null=True)

    def  __str__(self):
        return f'{self.ingredient_id}-{self.ingredient_name}'



class Recipes(models.Model):
    recipe_name = models.CharField(max_length = 100, null=True)
    recipe_id = models.PositiveIntegerField(null=True)

    cooking_time = models.PositiveIntegerField(null=True)  # Time is saved in minutes
    time_unit = models.CharField(max_length = 200, choices = unit_of_time, null=True)
    category = models.CharField(max_length = 200, choices = CATEGORY)
    number_of_serves = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=800, null=True)

    def  __str__(self):
        return f'{self.recipe_name}'

class keywords(models.Model):
    recipe_id = models.ForeignKey('Recipes', on_delete = models.CASCADE, null = True)
    keyword = models.CharField(max_length = 100, null=True)

    def  __str__(self):
        return f'{self.keyword}-{self.recipe_id}'

class userRecipes(models.Model):
        recipe_name = models.CharField(max_length = 100, null=True)
        recipe_id = models.PositiveIntegerField(null=True)
        cooking_time = models.PositiveIntegerField(null=True )
        time_unit = models.CharField(max_length = 200, choices = unit_of_time, null=True)
        category = models.CharField(max_length = 200, choices = CATEGORY)

        def  __str__(self):
            return f'{self.recipe_name}-{self.staff.username}'

class process_steps(models.Model):

    recipe_id = models.ForeignKey('Recipes', on_delete = models.CASCADE, null = True)
    step_no = models.PositiveIntegerField(null=True)
    utensil_id = models.ForeignKey('Utensils', on_delete = models.CASCADE, null = True)
    process = models.CharField(max_length = 100, null=True)
    ingredient_id = models.ForeignKey('Ingredients', on_delete = models.CASCADE, null = True)
    temperature = models.PositiveIntegerField(null=True)
    temperature_unit = models.CharField(max_length = 200, choices = unit_of_temperature, null = True )
    time = models.PositiveIntegerField(null=True)
    time_unit = models.CharField(max_length = 200, choices = unit_of_time, null=True)
    Quantity = models.PositiveIntegerField(null = True)
    Quantity_unit = models.CharField(max_length = 200, choices = unit_of_quantity, null = True )



    def  __str__(self):
        return f'{self.recipe_id}-{self.step_no}'

class ratings(models.Model):
     user_id = models.ForeignKey(User,on_delete = models.CASCADE, null = True, default= None)
     recipe_id = models.ForeignKey(Recipes, on_delete = models.CASCADE, null = True)
     rating = models.PositiveIntegerField(null=True, default = 0,

    validators=[
                MaxValueValidator(5),
                MinValueValidator(0),
    ]
     )  # if the rating is zero.. it means no user has rated it yet.

     def create_ratings(cls, rating):


         cls.rating = rating

         return cls

     def  __str__(self):
         return f'{self.pk}-{self.rating}'



class shared_recipes(models.Model):
     shared_by = models.ForeignKey(User,on_delete = models.CASCADE,related_name= 'shared_by_this_user', db_column='shared_by_this_user'  , null = True, default= None)
     shared_to = models.ForeignKey(User,on_delete = models.CASCADE,related_name= 'shared_to_this_user', db_column= 'shared_to_this_user', null = True, default= None)
     recipe_id = models.ForeignKey(Recipes, on_delete = models.CASCADE, null = True)

     def  __str__(self):
          return f'{self.shared_by}-{self.recipe_id}'

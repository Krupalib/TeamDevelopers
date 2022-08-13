from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class user_model(models.Model):
        username = models.CharField(max_length = 100, null=True)
        email = models.CharField(max_length = 100, null=True)



        def create_user_model(cls, username, email):

            cls.username = username
            cls.email = email

            return cls

        def  __str__(self):
            return f'{self.username}-{self.email}'

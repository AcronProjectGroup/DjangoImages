from django.db import models
from django.contrib.auth.models import AbstractUser


# You can use this for first you don't know CustomUser, what will have: 
# class CustomUser(AbstractUser):
#     pass



class CustomUser(AbstractUser):
    age = models.PositiveIntegerField()



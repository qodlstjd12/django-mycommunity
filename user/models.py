from django.contrib.auth.models import UserManager
from django.core.exceptions import TooManyFieldsSent
from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    university = models.CharField(max_length=15)

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
#     post_time = models.DateTimeField(auto_now_add=True)
#     body = models.CharField(max_length=500)

#     def __str__(self):
#         return self.title
    
#     def summary(self):
#         return self.body[:100]

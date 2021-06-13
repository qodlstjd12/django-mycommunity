from django.db import models
from user.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    post_time = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

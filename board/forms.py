from django.contrib.auth.models import User
from django.db.models import fields
from user import models
from django import forms
from board.models import Post
from user.models import User

class MyPageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'university']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']
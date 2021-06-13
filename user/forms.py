from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import fields
from django.contrib.auth import get_user_model
from django.forms.forms import Form
from .models import User
class LoginForm(forms.Form):
    class Meta:
        user = User()
        fields = ['username', 'password', 're_password']
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','nickname','password1','password2','university']

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title','body']

# class RegisterForm(forms.Form):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#             }
#         )
#     )
    
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )

#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )

#     def clean_userid(self):
#         username = self.cleaned_data['username']
#         if User.objects.filter(id=id).exists():
#             raise forms.ValidationError('이 아이디는 이미 사용중입니다')
#         return username
    
#     def clean_password(self):
#         password1 = self.cleaned_data['password1']
#         password2 = self.cleaned_data['password2']
#         if password1 != password2:
#             raise forms.ValidationError('비밀번호가 서로 일치하지 않습니다')
#         return password1

#     def register(self):
#         if self.is_valid():
#             return User.objects.create(
#                 username =self.cleaned_data['username'],
#                 password = self.cleaned_data['password1']
#             )
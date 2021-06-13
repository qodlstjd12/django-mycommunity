from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from board.models import Post
from .forms import LoginForm,RegisterForm

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils import timezone
# Create your views here.

def login_view(request):
    form = AuthenticationForm()
    return render(request, 'user/home.html', {'form':form})

@method_decorator(csrf_exempt, name='dispatch')
def mylogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request=request ,username=username, password=password)
            print('디버깅 문장 : ', username , 'X', password, 'X', user)
            if user is not None:
                print('로그인 성공')
                login(request, user)
                post = Post.objects.all()
            return render(request, 'board/home.html',{'user' : user, 'post' : post})
        else:
            print('로그인 실패')
            return HttpResponse('Not signed in')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user:home')
    return render(request, 'register.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect('user:home')


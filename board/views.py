from datetime import time
from user.models import User
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from board.forms import PostForm, MyPageForm
from django.utils import timezone
# Create your views here.

def home(request):
    post = Post.objects.all()
    return render(request, 'board/home.html', {'post':post})

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.post_time=timezone.now()
            post.save()
            return redirect('board:home')
    else:
        form = PostForm()
        return render(request,'board/new.html',{'post':form})

def detail_view(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'board/detail.html', {'post':post})

def mypage_view(request):
    return render(request, 'board/mypage.html')

def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('user:home')

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('board:home')

def update(request, id):
    post = Post.objects.get(id=id)
    if request.method =='POST':
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.post_time = timezone.now()
        post.save()
        return redirect('board:home')
    return render(request, 'board/update.html', {'post':post})
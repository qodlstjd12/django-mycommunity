from datetime import time
from user.models import User
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comment
from board.forms import CommentForm, PostForm, MyPageForm
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
    comment = Comment.objects.all()
    return render(request, 'board/detail.html', {'post':post, 'comment': comment})

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

def comment(request, id):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_form = form.save(commit=False)
            comment_form.user = request.user
            comment_form.post = get_object_or_404(Post, pk = id)
            comment_form.comment_time = timezone.now()
            comment_form.save()
            return redirect('board:detail', id)
    return redirect('board/detail')

def comment_delete(request, id, id2):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('board:detail', id2)

def message_view(request):
    return render(request, 'board/message.html')
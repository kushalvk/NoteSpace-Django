from django.shortcuts import render, redirect
from .models import Post
from .forms import RegisterForm
from django.contrib.auth import login

def home(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

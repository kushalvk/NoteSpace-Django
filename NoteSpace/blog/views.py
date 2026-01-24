from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import RegisterForm
from django.contrib.auth import login
from django.core.paginator import Paginator

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

def blog_list(request):
    posts = Post.objects.filter(status="published").order_by("-created_at")
    paginator = Paginator(posts, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/blog_list.html", {"page_obj": page_obj})

def category_post(request, slug):
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(category = category, status="published")

    return render(request, "blog/category_posts.html", {
        "category": category,
        "post": posts
    })
from django.shortcuts import render, redirect
from .models import Post, Category, Tag
from .forms import RegisterForm, TagForm, CategoryForm, PostForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden

# Default
def home(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

# Auth
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

# Blog
@login_required
def blog_list(request):
    posts = Post.objects.filter(status="published").order_by("-created_at")
    paginator = Paginator(posts, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/blog_list.html", {"page_obj": page_obj})

@login_required
def user_posts(request, username):
    user = get_object_or_404(User, username=username)

    posts = Post.objects.filter(author=user, status="published").order_by("-created_at")

    return render(request, "blog/user_posts.html", {
        "author": user,
        "posts": posts
    })

@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status="published")

    return render(request, "blog/post_detail.html", {
        "post": post
    })

# Category
@login_required
def category_post(request, slug):
    cat = Category.objects.get(slug = slug)
    posts = Post.objects.filter(category = cat, status="published")

    return render(request, "blog/category_posts.html", {
        "category": cat,
        "posts": posts
    })

def is_category_admin(user):
    return user.is_superuser or user.is_staff

@login_required
def manage_categories(request):
    categories = Category.objects.all().order_by("-id")
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_categories")

    return render(request, "blog/manage_categories.html", {
        "categories": categories,
        "form": form
    })

@login_required
def edit_category(request, id):
    if not is_category_admin(request.user):
        return HttpResponseForbidden("Not allowed")
    
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("manage_categories")
    else:
        form = CategoryForm(instance=category)

    return render(request, "blog/edit_category.html", {"form": form})

@login_required
def delete_category(request, id):
    if not is_category_admin(request.user):
        return HttpResponseForbidden("Not allowed")
    
    Category.objects.filter(id=id).delete()
    return redirect("manage_categories")

# Tags
@login_required
def manage_tags(request):
    tags = Tag.objects.all().order_by("-id")
    form = TagForm()

    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_tags")

    return render(request, "blog/manage_tags.html", {
        "tags": tags,
        "form": form
    })

@login_required
def edit_tag(request, id):
    if not is_category_admin(request.user):
        return HttpResponseForbidden("Not allowed")

    tag = get_object_or_404(Tag, id=id)

    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("manage_tags")
    else:
        form = TagForm(instance=tag)

    return render(request, "blog/edit_tag.html", {"form": form})

@login_required
def delete_tag(request, id):
    if not is_category_admin(request.user):
        return HttpResponseForbidden("Not allowed")

    Tag.objects.filter(id=id).delete()
    return redirect("manage_tags")

@login_required
def tag_posts(request, name):
    tag = get_object_or_404(Tag, name=name)
    posts = Post.objects.filter(tags=tag, status="published")

    return render(request, "blog/tag_posts.html", {
        "tag": tag,
        "posts": posts
    })

# Post
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect("blogs")
    else:
        form = PostForm()

    return render(request, "blog/create_post.html", {"form": form})

# Profile
def profile(request, username):
    user = get_object_or_404(User, username=username)

    post_count = Post.objects.filter(author=user, status="published").count()

    can_edit = request.user == user

    return render(request, "blog/profile.html", {
        "profile_user": user,
        "post_count": post_count,
        "can_edit": can_edit
    })

@login_required
def edit_profile(request):
    user = request.user

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile", username=user.username)
    else:
        form = ProfileForm(instance=user)

    return render(request, "blog/edit_profile.html", {"form": form})
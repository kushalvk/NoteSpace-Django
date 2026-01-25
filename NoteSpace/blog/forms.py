from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category, Tag, Post
from django import forms
from django.utils.text import slugify

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.slug = slugify(self.cleaned_data["name"])
        if commit:
            obj.save()
        return obj
    
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "category", "tags", "content", "image", "status"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 10}),
            "tags": forms.CheckboxSelectMultiple(),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
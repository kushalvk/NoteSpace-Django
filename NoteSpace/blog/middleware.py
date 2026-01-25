# blog/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        open_urls = [
            reverse("home"),
            reverse("register"),
            "/accounts/login/",   # Django default login URL
            "/accounts/logout/",
        ]

        if not request.user.is_authenticated and request.path not in open_urls:
            return redirect("/accounts/login/?next=" + request.path)

        return self.get_response(request)
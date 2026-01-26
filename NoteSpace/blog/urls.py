from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('blogs/', views.blog_list, name='blogs'),
    path('category/<slug:slug>/', views.category_post, name='category_posts'),
    path("dashboard/categories/", views.manage_categories, name="manage_categories"),
    path("dashboard/categories/edit/<int:id>/", views.edit_category, name="edit_category"),
    path("dashboard/categories/delete/<int:id>/", views.delete_category, name="delete_category"),
    path("dashboard/tags/", views.manage_tags, name="manage_tags"),
    path("dashboard/tags/edit/<int:id>/", views.edit_tag, name="edit_tag"),
    path("dashboard/tags/delete/<int:id>/", views.delete_tag, name="delete_tag"),
    path("dashboard/posts/create/", views.create_post, name="create_post"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("profile/<str:username>/posts/", views.user_posts, name="user_posts"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("blog/<slug:slug>/", views.post_detail, name="post_detail"),
    path("tag/<str:name>/", views.tag_posts, name="tag_posts"),
    path("search/", views.search, name="search"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("dashboard/drafts/", views.draft_posts, name="draft_posts"),
    path("dashboard/drafts/edit/<int:id>/", views.edit_draft, name="edit_draft"),
    path("dashboard/drafts/publish/<int:id>/", views.publish_draft, name="publish_draft"),
]
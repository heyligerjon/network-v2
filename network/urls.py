
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("status/<int:statusId>", views.status_view, name="status_view"),
    path("status/new", views.status_new, name="status_new"),
    path("status/<int:statusId>/edit", views.status_edit, name="status_edit"),
    path("user/<str:username>", views.profile_view, name="profile_view"),
    path("user/<str:username>/edit", views.profile_edit, name="profile_edit"),
    path("user/<str:username>/friends", views.friends_list, name="friends_list")
]

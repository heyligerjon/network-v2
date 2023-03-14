
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r"(?:/(?P<route>[a-zA-Z]+)/)?", views.index, name="index"),
    # path("login", views.login_view, name="login"),
    # path("logout", views.logout_view, name="logout"),
    # path("register", views.register, name="register"),
    # path("status/<int:statusId>", views.status_view, name="status_view"),
    # path("user/<str:username>", views.profile_view, name="profile_view"),
]

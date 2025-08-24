from django.urls import path
from django.contrib.auth import views as account_views
from . import views

urlpatterns = [
    path("register/", views.register, name='users-register'),
    path("login/",  account_views.LoginView.as_view(template_name='users/login.html'), name="users-login"),
    path("logout/", views.LogoutView.as_view(), name='users-logout')
]
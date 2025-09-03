from django.urls import path
from django.contrib.auth import views as account_views
from . import views

urlpatterns = [
    path("register/", views.register, name='users-register'),
    path(
        "login/",  
        account_views.LoginView.as_view(
            template_name='users/login.html', 
            extra_context={"loginActive": True, "title": "Влизане"}
        ), 
        name="users-login"
    ),
    path("logout/", views.LogoutView.as_view(), name='users-logout'),
    path("<int:profileId>", views.profileHomework, name="users-profileinfo"),
    path("backup", views.backup, name="users-backup")
]
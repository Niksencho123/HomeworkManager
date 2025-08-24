from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name='homework-home'),
    path("tomorrow/", views.Tomorrow.as_view(), name='homework-tomorrow'),
    path("operation/", views.operation, name='homework-operation')
]
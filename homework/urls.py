from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name='homework-home'),
    path("tomorrow/", views.Tomorrow.as_view(), name='homework-tomorrow'),
    path("all/", views.All.as_view(), name='homework-all'),
    path("add/", views.addAssignment, name='homework-add'),
    path("assignment/<int:homeworkId>/", views.assignmentInfo, name='homework-assignment')
]
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name='homework-home'),
    path("tomorrow/", views.Tomorrow.as_view(), name='homework-tomorrow'),
    path("all/", views.All.as_view(), name='homework-all'),
    path("add/", views.addAssignment, name='homework-add'),
    path("assignment/<int:homeworkId>/", views.assignmentInfo, name='homework-assignment'),
]

if settings.DEBUG:
    urlpatterns.append(path("vote/<str:code>", views.surveyInfo, name='homework-surveyInfo'))
    urlpatterns.append(path("vote/", views.surveyEntry, name='homework-surveyEntry'))
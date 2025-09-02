from django.urls import path
from .views import *

urlpatterns = [
    path("", messaging, name='messages-main')
]

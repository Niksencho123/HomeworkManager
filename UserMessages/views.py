from django.shortcuts import render
from django.views import View

# Create your views here.
def messaging(request):
    return render(request, "UserMessages/base.html")
from django.shortcuts import render
from django.views import View
from django.utils import timezone
from django.http import HttpResponse
from . import models

# Create your views here.
class Home(View):
    def get(self, request):
        now = timezone.now()
        active_messages = models.Messages.objects.filter(dateBegin__lte=now, dateEnd__gte=now)
        context = {
            "homeActive": True,
            "activeMessages": active_messages
        }
        return render(request, "homework/home.html", context)
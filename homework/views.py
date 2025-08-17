from django.shortcuts import render
from django.views import View
from django.utils import timezone
from django.http import HttpResponse
from datetime import timedelta
from . import models

# Create your views here.

# *Засега е готово, май :)
class Home(View):
    def get(self, request):
        now = timezone.now()
        activeMessages = models.Messages.objects.filter(dateBegin__lte=now, dateEnd__gte=now)
        context = {
            "homeActive": True,
            "activeMessages": activeMessages,
            "title": "Начална страница"
        }
        return render(request, "homework/home.html", context)

class Tomorrow(View):
    def get(self, request):
        tomorrowDate = timezone.now().date() + timedelta(days=1)
        tomorrowHomework = models.Assignment.objects.filter(dateDue=tomorrowDate)
        context = {
            "tomorrowActive": True,
            "homework": tomorrowHomework,
            "title": "Утрешни задания"
        }
        return render(request, "homework/tomorrow.html", context=context)
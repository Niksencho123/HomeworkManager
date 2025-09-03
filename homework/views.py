from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import HttpResponse
from datetime import timedelta
from django.contrib.auth.forms import UserCreationForm
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
# За предпочитане е да се използва вече ListView
# class Tomorrow(View):
#     def get(self, request):
#         tomorrowDate = timezone.now().date() + timedelta(days=1)
#         tomorrowHomework = models.Assignment.objects.filter(dateDue=tomorrowDate)
#         paginatorObj = Paginator(tomorrowHomework, 3)
#         pageNumber = request.GET.get("page")

#         homeworkObj = paginatorObj.get_page(pageNumber)
#         context = {
#             "tomorrowActive": True,
#             "homework": homeworkObj,
#             "title": "Утрешни задания"
#         }
#         return render(request, "homework/tomorrow.html", context=context)
    
class TomorrowTest(ListView):
    model = models.Assignment
    template_name = "homework/tomorrow.html"
    context_object_name = "assignments"
    paginate_by = 2
    def get_queryset(self):
        tomorrow = timezone.localdate() + timedelta(days=1)
        return models.Assignment.objects.filter(dateDue=tomorrow)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tomorrowActive'] = True
        context['title'] = "Утрешни задания"
        return context


def assignmentInfo(request, homeworkId):
    result = models.Assignment.objects.get(id=homeworkId)
    return render(request, "homework/assignment.html", context={"assignment": result, "title": f"Задание №{result.id}"})
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.views import View
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import HttpResponse
from datetime import timedelta
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from . import forms
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

class Tomorrow(ListView):
    model = models.Assignment
    template_name = "homework/tomorrow.html"
    context_object_name = "assignments"
    paginate_by = 20
    def get_queryset(self):
        today = timezone.localdate()
        tomorrow = today + timedelta(days=1)
        return (
            models.Assignment.objects
            .filter(dateDue__in=[today, tomorrow])
            .order_by("-dateDue")
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tomorrowActive'] = True
        context['title'] = "Утрешни задания"
        return context
class All(ListView):
    model = models.Assignment
    template_name = "homework/all.html"
    context_object_name = "assignments"
    paginate_by = 10
    def get_queryset(self):
        return models.Assignment.objects.all().order_by("-dateDue")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allActive'] = True
        context['title'] = "Всички задания"
        return context

def addAssignment(request):
    today = timezone.now().date()
    activeDuties = models.DutyStudent.objects.filter(
        dateBegin__lte=today,
        dateEnd__gte=today
    )
    allUsers = User.objects.select_related("studentprofile").order_by("studentprofile__classNumber")
    if request.method == "POST":
        form = forms.AssignmentAdd(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.addedBy = request.user
            assignment.save()
            messages.success(request, f"Заданието беше добавено ")
            return redirect("homework-home")
        else:
            return render(request, "homework/add.html", {"form": form})
    else:
        form = forms.AssignmentAdd()
    return render(request, "homework/add.html", {"form": form, "activeDuties": activeDuties, "users":allUsers, "addActive": True, "title": "Добавяне на задание"})



def assignmentInfo(request, homeworkId):
    today = timezone.now().date()
    activeDuties = models.DutyStudent.objects.filter(
        dateBegin__lte=today,
        dateEnd__gte=today
    )
    result = models.Assignment.objects.get(id=homeworkId)
    if request.method == "POST":
        form = forms.AssignmentAdd(request.POST,instance=result)
        if form.is_valid():
            messages.success(request, f"Заданието беше актуализирано")
            form.save()
            return redirect("homework-home")
        else:
            return render(request, "homework/assignment.html", {"form": form})
    else:
        form = forms.AssignmentAdd(instance=result)
    return render(request, "homework/assignment.html", context={"assignment": result, "duties": activeDuties,"form": form, "title": f"Задание №{result.id}"})
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.views import View
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from datetime import timedelta
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required, user_passes_test
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

def isPartOfClass(user):
    if user.studentprofile.classNumber >= 1 and user.studentprofile.classNumber <= 25:
        return True
    else:
        return False

@login_required
@user_passes_test(isPartOfClass, redirect_field_name="homework-home")
def surveyInfo(request, code):
    if request.method == "POST":
        question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "",
            {
                "question": question,
                "error_message": "Не беше избран",
            },
        )
    else:
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    if request.method == "GET":
        try:
            questionInfo = models.Question.objects.get(questionCode=code)
        except models.Question.DoesNotExist:
            raise Http404("Този код не е намерен!")
        return render(request, "homework/surveyInfo.html", context = {"question": questionInfo})

@login_required
@user_passes_test(isPartOfClass, redirect_field_name="homework-home")
def surveyEntry(request):
    if request.method == "POST":
        return redirect("homework-surveyInfo", code=request.POST.get("code"))
    return render(request, "homework/surveyEntry.html")
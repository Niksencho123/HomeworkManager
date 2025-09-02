from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.urls import resolve
from django.contrib import messages
from .forms import SignUpForm, ProfileUpdate, UserUpdate
from django.http import Http404
from .models import StudentProfile
import os
import zipfile
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")

            messages.success(request, f"Профилът беше добавен")
            return redirect("homework-home")
        else:
            return render(request, "users/register.html", {"form": form})
    else:
        form = SignUpForm()
    return render(request, "users/register.html", {"form": form, "registerActive": True})

from django.contrib.auth import logout
from django.views import View


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        messages.success(request, message="Излезнахте от акаунта си :(")
        logout(request)
        return redirect('homework-home')

@login_required
def profileHomework(request, profileId):
    try:
        lookupUser = User.objects.get(id=profileId)
    except User.DoesNotExist:
        raise Http404("Потребителят не е намерен")
    context = {
        "userInfo": lookupUser,
    }
    if request.user.is_authenticated:
        if request.user.id == profileId:
            context["title"] = f"Вашият профил"
            context["profileViewOwn"] = True
        else:
            context["title"] = f"Профил №{profileId}"
    else:
        context["title"] = f"Профил №{profileId}"
    if request.method == "POST":
        userform = UserUpdate(request.POST, instance=request.user)
        profileform = ProfileUpdate(request.POST, request.FILES, instance=request.user.studentprofile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect("users-profileinfo", profileId=request.user.id)
    else:
        userform = UserUpdate(instance=request.user)
        profileform = ProfileUpdate(request.FILES, instance=request.user.studentprofile)
    context["userform"] = userform
    context["profileform"] = profileform
    return render(request, "users/account-homework.html", context=context)

def is_special_user(user):
    return user.is_authenticated and user.username == 'Niksencho'

@user_passes_test(is_special_user, redirect_field_name='homework-home')
def backup(request):
    # Paths
    db_path = settings.DATABASES['default']['NAME']  # SQLite path
    media_path = settings.MEDIA_ROOT
    zip_filename = "backup.zip"

    # Create ZIP in memory
    zip_path = os.path.join(settings.BASE_DIR, zip_filename)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add DB
        if os.path.exists(db_path):
            zipf.write(db_path, os.path.basename(db_path))
        # Add media folder
        for foldername, subfolders, filenames in os.walk(media_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zipf.write(file_path, os.path.relpath(file_path, settings.BASE_DIR))

    # Serve the ZIP file
    with open(zip_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="application/zip")
        response['Content-Disposition'] = f'attachment; filename={zip_filename}'
    
    # Optional: delete the zip after sending
    os.remove(zip_path)
    
    return response

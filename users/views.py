from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Профилът беше добавен")
            return redirect("homework-home")
        else:
            return render(request, "users/register.html", {"form": form})
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

from django.contrib.auth import logout
from django.views import View

class LogoutView(View):
    def get(self, request):
        messages.success(request, message="Излезнахте от акаунта си :(")
        logout(request)
        return redirect('homework-home')
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Message

# Create your views here.
@login_required
def messaging(request):
    if request.method == "POST":
        messageText = request.POST.get("new-message")
        Message.objects.create(userConn = request.user, message = messageText)
        return redirect("messages-main")
    allMessages = Message.objects.all()[::-1]
    context = {
        "posts": allMessages
    }
    return render(request, "UserMessages/home.html", context)
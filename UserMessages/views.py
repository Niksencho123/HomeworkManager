from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
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
    paginator = Paginator(allMessages, 10)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    context = {
        "posts": posts,
        "title": "Чатове"
    }
    return render(request, "UserMessages/home.html", context)
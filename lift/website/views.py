from django.shortcuts import render
from django.http import HttpResponse

from .models import Pipes
from .forms import PostForm
# Create your views here.

def welcome_view(request):
    return render(request, "website/welcome.html",{"welcome_view": welcome_view})

def form_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()  #blank form
    return render(request, "website/form.html", {"form": form})
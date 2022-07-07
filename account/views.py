from django.shortcuts import redirect, render
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt 
from .models import User 
import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from school.views import index

def home(request):
    return render(request, 'index.html')

@csrf_exempt 
def user_signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        User.objects.create(email=email,username=username,password=make_password(password))
    return render(request, "authentication/signup.html")

@csrf_exempt 
def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        context["name"] = user
        print(username)
        print(password)
        print(context)
        if user is not None:
            login( request,user)
            print("user is not None")
            return HttpResponseRedirect(reverse(index))
        else:
            print("user is None")
            raise Http404()

    return render(request, "authentication/login.html",context)
    
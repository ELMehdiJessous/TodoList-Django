from django.shortcuts import render ,redirect
from .forms import *
from django.contrib.auth import login as auth_login,authenticate,logout as auth_logout
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect("todo")
    else:
        form = signupform()
    return render(request,"accounts/signup.html",{'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username,password=password)
        
        if user is not None:
            auth_login(request,user)
            return redirect("todo")
    return render(request, "accounts/login.html")

def logout(request):
    auth_logout(request)
    return redirect("login")
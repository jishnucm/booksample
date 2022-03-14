from django.shortcuts import render
from django.http import HttpResponse


def books(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def slogin(request):
    return render(request,'slogin.html')

def ssignup(request):
    return render(request,'ssignup.html')
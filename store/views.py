from django.shortcuts import render
from django.http import HttpResponse


def books(request):
    return render(request,'index.html')

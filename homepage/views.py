from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'home.html')


def none(request):
    return HttpResponse("Die")
# Create your views here.

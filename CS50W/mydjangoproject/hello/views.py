from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request=request,template_name="hello/index.html")

def brian(request):
    return HttpResponse("Brian")

def rwanda(request):
    return HttpResponse("Amazing country of Rwanda")


def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})

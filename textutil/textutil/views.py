from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")

def removepunc(request):
    return render(request,"removepunc.html")

def capitalizefirst(request):
    return render(request,"capitalizefirst.html")

def newlineremover(request):
    return render(request,"newlineremover.html")

def spaceremover(request):
    return render(request,"spaceremover.html")

def charcount(request):
    return render(request,"charcount.html")
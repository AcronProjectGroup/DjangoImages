from django.shortcuts import render
from django.http import HttpResponse

def LovePizza(request):
    return HttpResponse("I Love Pizza")

def LoveHamburger(request):
    return HttpResponse("I Love Hamburger")


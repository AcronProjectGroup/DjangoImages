from django.shortcuts import render
from django.http import HttpResponse


def sayHello(request):
    return HttpResponse("""
    <br>Project
    
    <br>Django
    
    <br>Acron
    
    <br>Sina""")

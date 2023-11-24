from django.shortcuts import render
from django.http import HttpResponse


def sayHello(request):
    return HttpResponse("""
    <br>Hello
    
    <br>Hello
    
    <br>Hello
    
    <br>Hello""")

from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, 'pages/home.html')

def manifest_consciousness(request):
    return render(request, 'pages/manifest-consciousness.html')





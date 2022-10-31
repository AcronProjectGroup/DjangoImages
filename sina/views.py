from django.shortcuts import render
from django.http import HttpResponse


def intro_sina(request):
    return render(request, 'sina/lale.html')

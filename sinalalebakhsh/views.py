from django.shortcuts import render
from django.http import HttpResponse


def i_am_sina(request):
    return render(request, 'templates/sinalalebakhsh/sinalalebakhsh.html')








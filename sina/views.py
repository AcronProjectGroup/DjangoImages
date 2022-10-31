from django.shortcuts import render
from django.http import HttpResponse


def intro_sina(request):
    return HttpResponse('sina lalebakhsh is here')

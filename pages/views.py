from django.shortcuts import render

from django.http import HttpResponse


def say_hellos(request):
    return HttpResponse('HOME page is here...[*]')




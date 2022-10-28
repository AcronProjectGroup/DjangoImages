from django.shortcuts import render

from django.http import HttpResponse


def say_hellos(request):
    return HttpResponse('All pages is here...[*]')




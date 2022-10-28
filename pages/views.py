from django.shortcuts import render

from django.http import  HttpResponse

def say_hello(request):
    return HttpResponse('All pages is here...[*]')




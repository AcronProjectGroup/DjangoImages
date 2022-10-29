from django.shortcuts import render

from django.http import HttpResponse


def home_view(request):
    return HttpResponse('HOME page is here...[*]')


def about_view(request):
    return  HttpResponse('ABOUT page 4U.')


def contactus_view(request):
    return  HttpResponse('Contactus = Sina,IRAN, Tehran.')



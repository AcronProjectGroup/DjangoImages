from django.shortcuts import render

from django.http import HttpResponse


def home_view(request):
    return render(request, 'acron_project.html')


def about_view(request):
    return  HttpResponse('ABOUT page 4U.')


def contactus_view(request):
    return  HttpResponse('Contactus = Sina,IRAN, Tehran.')



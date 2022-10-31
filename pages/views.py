from django.shortcuts import render

from django.http import HttpResponse


def home_view(request):
    context = {
        'Page_name': 'AcronProject-HomePage',
        'description': 'Acron project is for everyone of Consciousness.'
    }
    return render(request, 'acron_project.html', context)


def about_view(request):
    return  HttpResponse('ABOUT page 4U.')


def contactus_view(request):
    return  HttpResponse('Contactus = Sina,IRAN, Tehran.')



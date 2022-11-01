from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    context = {
        'Page_name': 'AcronProject-HomePage',
        'description': 'Acron project is for everyone of Consciousness.',
    }
    return render(request, 'pages/home.html', context)


def consciousness(request):
    return render(request, 'pages/consciousness.html')


def manifest_consciousness(render):
    return render(request, 'pages/manifest-consciousness.html')





from django.shortcuts import render

from django.http import HttpResponse


def home_view(request):
    context = {
        'Page_name': 'AcronProject-HomePage',
        'description': 'Acron project is for everyone of Consciousness.',
    }
    return render(request, 'acron_project.html', context)






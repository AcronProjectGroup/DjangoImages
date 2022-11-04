from django.shortcuts import render
from django.http import HttpResponse
from .models import Note




#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------


def home_view(request):
    notes = Note.objects.all()
    context = {
        'Page_name': 'AcronProject-HomePage',
        'description': 'Acron project is for everyone of Consciousness.',
        'notes': notes,
    }
    return render(request, 'pages/home.html', context)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------


def consciousness(request):
    return render(request, 'pages/consciousness.html')

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

def manifest_consciousness(request):
    return render(request, 'pages/manifest-consciousness.html')





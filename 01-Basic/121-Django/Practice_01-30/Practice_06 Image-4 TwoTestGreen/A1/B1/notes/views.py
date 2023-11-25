from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

# Django ORM
def notes_list_view(resquest):
    # db -> notes -> view -> template
    
    # default manager
    notes = Note.objects.all() 
    context = {
        "notes_list": notes,
    }

    # Test this:
    # print(notes)
     
    return render(resquest, "notes/notes_list.html", context)
from django.shortcuts import render
from django.http import HttpResponse

def notes_list_view(resquest):
    return render(resquest, "notes/notes_list.html")
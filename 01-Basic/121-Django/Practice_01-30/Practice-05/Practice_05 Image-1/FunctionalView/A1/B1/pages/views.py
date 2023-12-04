from django.shortcuts import render
from django.http import HttpResponse

def home_page_view(request):
    return render(request, "home.html")

def about_page_view(request):
    context = {
        "page_name": "About",
        "description": "This part is about our team."
    }
    return render(request, "pages/about.html", context)

def contactus_page_view(request):
    return render(request, "pages/contactus.html")


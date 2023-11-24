from django.shortcuts import render
from django.http import HttpResponse

def home_page_view(request):
    return render(request, "home.html")

def about_page_view(request):
    return render(request, "pages/about.html")

def contactus_page_view(request):
    return HttpResponse("contactus_page_view")


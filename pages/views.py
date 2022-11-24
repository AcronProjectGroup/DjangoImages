from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


def homeredirectview(request):
    return redirect('home') 


class HomeView(TemplateView):
    template_name = 'home.html'



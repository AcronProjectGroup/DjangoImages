from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'



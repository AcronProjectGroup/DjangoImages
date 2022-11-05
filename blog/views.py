from django.shortcuts import render
from django.http import HttpResponse


def blog_view(request):
    return HttpResponse('Blog is here ... [*]')

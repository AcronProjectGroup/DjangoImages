from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Post

def post_list_view(request):
    posts_list = Post.objects.all()
    return render(request, "blog/posts_list.html", {"posts_list": posts_list})


def post_detail_view(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except ObjectDoesNotExist:
        post = None
    return render(request, "blog/post_detail.html", {"post": post})




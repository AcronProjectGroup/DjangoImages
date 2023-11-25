from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def post_list_view(request):
    posts_list = Post.objects.all()
    return render(request, "blog/posts_list.html", {"posts_list": posts_list})


def post_detail_view(request, id):
    print("ID:", id)
    return HttpResponse(f"Id: {id}")




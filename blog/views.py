from django.shortcuts import render

from .models import Post


def blog_view(request):
    post_list = Post.objects.all()
    return render(request,'blog/blog.html', {'post_list': post_list})

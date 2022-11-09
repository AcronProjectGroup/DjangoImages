from django.shortcuts import render

from .models import Post


def blog_view(request):
    post_list = Post.objects.all()
    return render(request,'blog/blog.html', {'post_list': post_list})


def blog_detail_view(request, pk):
    get_pk_post_from_database = Post.objects.get(pk=pk)
    return render(request, 'blog/blog_post_detail.html', {'post': get_pk_post_from_database})



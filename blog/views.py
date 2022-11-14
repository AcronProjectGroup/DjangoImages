from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


from .models import Post


def blog_view(request):
    # post_list = Post.objects.all()  #ORM  object-relational mapper
    post_list = Post.objects.filter(status='pub')
    return render(request,'blog/blog.html', {'post_list': post_list})


def blog_detail_view(request, pk):
    try:
        get_pk_post_from_database = Post.objects.get(pk=pk)
        return render(request, 'blog/blog_post_detail.html', {'post': get_pk_post_from_database})
    except ObjectDoesNotExist:
        return render(request, 'pages/page_404.html')


def post_new_post(request):
    if request.method == 'POST':
        post_title = request.POST.get('title')
        post_text = request.POST.get('text')

        user = User.objects.all()[0] #ORM  object-relational mapper
        Post.objects.create(title=post_title, text=post_text, author=user, status='pub')
    else:
        print('GET')
    return render(request, 'blog/post_new_post.html')

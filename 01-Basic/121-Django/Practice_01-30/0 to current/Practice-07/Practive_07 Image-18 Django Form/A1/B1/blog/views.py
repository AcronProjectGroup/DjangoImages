from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Post
from .forms import NewPostForm


def post_list_view(request):
    # posts_list = Post.objects.all()
    posts_list = Post.objects.filter(status="pub")
    return render(request, "blog/posts_list.html", {"posts_list": posts_list})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})
    # try:
    #     post = Post.objects.get(pk=pk)
    # except ObjectDoesNotExist:
    # except Post.DoesNotExist:
    #     post = None


def post_add_view(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            form = NewPostForm()
    else:
        form = NewPostForm()
    return render(request, "blog/post_create.html", context={"form": form})

    # if request.method == 'POST': #  <--------------- This aproach have validation problems
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #     user = User.objects.all()[0] # Django ORM work in here
    #     Post.objects.create(title=post_title, text=post_text, author=user, status='pub')

    # else:
    #     print('get request')
    # return render(request, "blog/post_create.html")

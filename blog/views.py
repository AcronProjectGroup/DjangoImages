from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .forms import PostFormModel


# class-based view -------------------------------------------------------------------------------------
class BlogView(generic.ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by("-date_time_modified")
    
class BlogDetailView(generic.DetailView):
    template_name = 'blog/blog_post_detail.html'
    model = Post
    context_object_name = 'post'

class NewPostBlog(generic.CreateView):
    form_class = PostFormModel
    template_name = 'blog/post_new_post.html'

class UpdatePostBlog(generic.UpdateView):
    form_class = PostFormModel
    template_name = 'blog/update_post.html'
    model = Post

class DeletePostBlog(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog')
        

# Functional View -------------------------------------------------------------------------------------
# def blog_view(request):
    # post_list = Post.objects.all()  #ORM  object-relational mapper
    # post_list = Post.objects.filter(status='pub').order_by("-date_time_modified")
    # return render(request,'blog/blog.html', {'post_list': post_list})
#--------------------------------------------------------------------------------------------------------
# def blog_detail_view(request, pk):
#     try:
#         get_pk_post_from_database = Post.objects.get(pk=pk)
#         return render(request, 'blog/blog_post_detail.html', {'post': get_pk_post_from_database})
#     except ObjectDoesNotExist:
#         return render(request, 'pages/page_404.html')
#--------------------------------------------------------------------------------------------------------
# def post_new_post(request):
#     if request.method == 'POST':
#         submitted_form = PostFormModel(request.POST)
#         if submitted_form.is_valid():
#             submitted_form.save()
#             return redirect('blog')
#     else: #GET request
#         submitted_form = PostFormModel()
#     return render(request, 'blog/post_new_post.html', context= {'form': submitted_form})
    # -------------------------------------------------------------------------------------
    # if request.method == 'POST':
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #     user = User.objects.all()[0] #ORM  object-relational mapper
    #     Post.objects.create(title=post_title, text=post_text, author=user, status='pub')
    # else:
    #     print('GET')
    # return render(request, 'blog/post_new_post.html')
#--------------------------------------------------------------------------------------------------------
# def update_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostFormModel(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('blog_detail_view' ,form.id)
#     return render(request, 'blog/update_post.html', context={'form': form, 'post': post})
#--------------------------------------------------------------------------------------------------------
# def delete_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         post.delete()
#         return redirect('blog')
#     return render(request, 'blog/delete_post.html', context={'post': post})



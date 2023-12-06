from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm

# Class based view ===============================Class List View===============================
class PostListView(generic.ListView):
    model = Post
    template_name = "blog/posts_list.html"
    context_object_name = "posts_list"
    def get_queryset(self):
        return Post.objects.filter(status="pub").order_by("-datatime_modified")
# Class based view ===============================Class List View===============================
class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
# Class based view ===============================Class List View===============================
class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = "blog/post_create.html"
# Class based view ===============================Class List View===============================
class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_create.html"
# Class based view ===============================Class List View===============================
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("posts_list")
    # def get_success_url(self):
    #     return reverse("posts_list")





# Functional View --------------------------------Function List View---------------------------
    # def post_list_view(request):
    #     # posts_list = Post.objects.all()
    #     posts_list = Post.objects.filter(status="pub").order_by("-datatime_modified")
    #     return render(request, "blog/posts_list.html", {"posts_list": posts_list})
# Functional View --------------------------------Function List View---------------------------
    # def post_detail_view(request, pk):
    #     post = get_object_or_404(Post, pk=pk)
    #     return render(request, "blog/post_detail.html", {"post": post})
    #     # try:
    #     #     post = Post.objects.get(pk=pk)
    #     # except ObjectDoesNotExist:
    #     # except Post.DoesNotExist:
    #     #     post = None
# Functional View --------------------------------Function List View---------------------------
    # def post_add_view(request):
    #     if request.method == "POST":
    #         form = PostForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             form = PostForm()
    #             post = Post.objects.last()
    #             return render(request, "blog/post_detail.html", {"post": post})
    #     else:
    #         form = PostForm()
    #     return render(request, "blog/post_create.html", context={"form": form})
    #     # if request.method == 'POST': #  <--------------- This aproach have validation problems
    #     #     post_title = request.POST.get('title')
    #     #     post_text = request.POST.get('text')
    #     #     user = User.objects.all()[0] # Django ORM work in here
    #     #     Post.objects.create(title=post_title, text=post_text, author=user, status='pub')
    #     # else:
    #     #     print('get request')
    #     # return render(request, "blog/post_create.html")
# Functional View --------------------------------Function List View---------------------------
    # send this example to below:
    # blog/1/update  OR blog/13/update
    # def post_update_view(request, pk):
    #     post = get_object_or_404(Post, pk=pk)
    #     form = PostForm(request.POST or None,instance=post)
    #     if form.is_valid():
    #         form.save()
    #         return render(request, "blog/post_detail.html", {"post": post})
    #     return render(request, "blog/post_create.html", context={"form": form, "post": post})
# Functional View --------------------------------Function List View---------------------------
    # def post_delete_view(request, pk):
    #     post = get_object_or_404(Post, pk=pk)
    #     if request.method == "POST":
    #         post.delete()
    #         return redirect("posts_list")
    #     return render(request, "blog/post_delete.html", context={"post": post,})








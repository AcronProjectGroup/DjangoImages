from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required



class PostListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'post/post_list.html'
    context_object_name = 'posts'


    
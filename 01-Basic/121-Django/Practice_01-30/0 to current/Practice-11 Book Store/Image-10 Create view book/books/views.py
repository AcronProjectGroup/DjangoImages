from django.shortcuts import render
from django.views import generic

from .models import Book

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DeleteView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price']
    template_name = 'books/book_create.html'    
    







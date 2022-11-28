from django.views import generic

from .models import Book

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list_view.html'
    context_object_name = 'books'


class BookDetailView(generic.DeleteView):
    model = Book
    template_name = 'books/book_detail_view.html'
    context_object_name = 'book'



class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'bokk_author', 'book_description', 'price']
    template_name = 'books/create_new_book.html'


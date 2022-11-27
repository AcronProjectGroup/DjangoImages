from django.views import generic

<<<<<<< HEAD
from .models import BookModel

class BookListView(generic.ListView):
    model = BookModel
    template_name = 'books/book_list_view.html'
=======
from .models import Book

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list_view.html'
    context_object_name = 'books'
<<<<<<< HEAD
>>>>>>> book_app_ver2
=======


class BookDetailView(generic.DeleteView):
    model = Book
    template_name = 'books/book_detail_view.html'
    context_object_name = 'book'

>>>>>>> book_app_ver2

from django.views import generic

from .models import BookModel

class BookListView(generic.ListView):
    model = BookModel
    template_name = 'books/book_list_view.html'

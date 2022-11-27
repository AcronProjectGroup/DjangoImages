from django.views import generic

from .models import BookModel

class BookListView(generic.ListView):
    model = BookModel
    

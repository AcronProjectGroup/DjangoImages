from django.urls import path

from .views import BookListView
from .views import BookDetailView
from .views import BookCreateView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('new/', BookCreateView.as_view(), name="book_create"),
]



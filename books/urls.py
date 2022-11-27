from django.urls import path

from .views import BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name="book_list_view"),
<<<<<<< HEAD
<<<<<<< HEAD
]
=======
=======
    path('<int:pk>/', BookDetailView.as_view(), name="book_detail_view"),
>>>>>>> book_app_ver2
    #Don't forget cama ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
]


>>>>>>> book_app_ver2

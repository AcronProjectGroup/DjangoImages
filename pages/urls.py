from django.urls import path
from .views import say_hellos


urlpatterns = [
    path('pages/', say_hellos, name="pages"),
]



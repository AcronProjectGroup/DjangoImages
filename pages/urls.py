from django.urls import path
from .views import say_hellos


urlpatterns = [
    path('', say_hellos, name="pages"),
]



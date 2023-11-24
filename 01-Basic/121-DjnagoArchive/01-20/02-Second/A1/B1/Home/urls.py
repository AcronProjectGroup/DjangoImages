from django.urls import path
from .views import sayHello

urlpatterns = [
    path("hi/", sayHello, name="Home")    
]

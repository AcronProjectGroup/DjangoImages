from django.urls import path
from .views import sayHello

urlpatterns = [
    path("", sayHello, name="Home")    
]
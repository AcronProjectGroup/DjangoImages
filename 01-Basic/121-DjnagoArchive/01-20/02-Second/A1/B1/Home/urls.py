from django.urls import path
from .views import sayHello

urlpatterns = [
    path("welcome", sayHello, name="Home")    
]

from django.urls import path
from .views import LovePizza, LoveHamburger

urlpatterns = [
    path("pizza/", LovePizza, name="Pizza"),
    path("hamburger/", LoveHamburger, name="Hamburger"),
]


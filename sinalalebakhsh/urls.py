from django.urls import path
from . import views



urlpatterns = [
    path('', views.i_am_sina, name="sinalalebakhsh"),
]




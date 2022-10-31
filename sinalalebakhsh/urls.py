from django.urls import path
from . import views



urlpatterns = [
    path('sinalalebakhsh/', views.i_am_sina, name="sinalalebakhsh"),
]




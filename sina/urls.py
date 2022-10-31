from django.urls import path
from . import views




urlpatterns = [
    path('', views.intro_sina, name="sina"),

]


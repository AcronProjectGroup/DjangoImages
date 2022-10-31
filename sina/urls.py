from django.urls import path
from . import views




urlpatterns = [
    path('sina/', views.intro_sina, name="sina"),

]


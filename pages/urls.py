from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeredirectview , name="homeredirect"),
    path('home/', views.HomeView.as_view() , name="home"),    
]




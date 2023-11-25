from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page_view, name="home"),
    path("about/", views.about_page_view, name="about"),
    path("contactus/", views.contactus_page_view, name="contactus"),
]

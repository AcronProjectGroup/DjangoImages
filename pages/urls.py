from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name="homepage"),
    path('consciousness/', views.consciousness, name="consciousness"),
    path('manifest-consciousness/', views.manifest_consciousness, name="manifest-consciousness"),
]





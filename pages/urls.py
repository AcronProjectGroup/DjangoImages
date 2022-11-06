from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name="homepage"),
    path('manifest-consciousness/', views.manifest_consciousness, name="manifest-consciousness"),
]





from django.urls import path
from .views import i_am_sina



urlpatterns = [
    path('', i_am_sina, name="home"),
]

## test 123



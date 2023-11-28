from django.urls import path

from . import views

urlpatterns = [
    path("", views.post_list_view, name="posts_list"),
    path("<int:pk>/", views.post_detail_view , name="post_detail"),
    path("<int:pk>/update", views.post_update_view, name="post_update"),
    path("add/", views.post_add_view, name="post_create"),
]

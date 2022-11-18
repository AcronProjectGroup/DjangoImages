from django.urls import path
from . import views


urlpatterns =[
    path('', views.BlogView.as_view(), name="blog"),
    path('<int:pk>', views.BlogDetailView.as_view(), name="blog_detail_view"),
    path('new/', views.NewPostBlog.as_view(), name="post_new_post"),
    path('<int:pk>/update/', views.update_post, name="update_post"),
    path('<int:pk>/delete/', views.delete_post, name="delete_post"),
]


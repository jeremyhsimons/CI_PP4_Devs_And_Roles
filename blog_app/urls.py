from django.urls import path
from . import views


urlpatterns = [
    path('blog_list/', views.BlogsList.as_view(), name="blog_list"),
    path('create_blog_post/', views.WriteBlog.as_view(),
         name='create_blog_post'),
    path('blog_detail/<slug:slug>', views.BlogView.as_view(),
         name='blog_detail'),
    path('edit_blog/<slug:slug>', views.UpdateBlog.as_view(),
         name='edit_blog'),
]

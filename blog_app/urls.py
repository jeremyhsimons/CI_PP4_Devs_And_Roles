from django.urls import path
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from . import views


urlpatterns = [
    path('blog_list/', views.BlogsList.as_view(), name="blog_list"),
    path('create_blog_post/', views.WriteBlog.as_view(),
         name='create_blog_post'),
    path('blog_detail/<slug:slug>', views.BlogView.as_view(),
         name='blog_detail'),
    path('edit_blog/<slug:slug>', views.UpdateBlog.as_view(),
         name='edit_blog'),
    path('delete_blog/<slug:slug>', views.delete_blog, name="delete_blog"),
    path('delete_comment/<int:comment_id>', views.delete_comment,
         name='delete_comment'),
    path('report_blog/<slug:slug>', views.report_blog, name='report_blog'),
    path('report_comment/<int:pk>', views.report_comment,
         name='report_comment'),
]

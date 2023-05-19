from django.urls import path
from . import views


urlpatterns = [
    path('blog_list/', views.BlogsList.as_view(), name="blog_list"),
]

from . import views
from django.urls import path


urlpatterns = [
    path('', views.JobPostingList.as_view(), name="home"),
    path(
        '<int:pk>/', views.JobPostingDetail.as_view(), name="job-post-detail"),
]

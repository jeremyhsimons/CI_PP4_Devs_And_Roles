from . import views
from django.urls import path


urlpatterns = [
    path('', views.JobPostingList.as_view(), name="home"),
    path(
        '<int:pk>/', views.JobPostingDetail.as_view(), name="job-post-detail"),
    path('create-job-post/', views.CreateJobPosting.as_view(),
         name="create-job-post"),
    path('update-job-post/', views.UpdateJobPosting.as_view(),
         name='update-job-post')
]

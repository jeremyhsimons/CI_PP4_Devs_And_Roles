from . import views
from django.urls import path


urlpatterns = [
    path('', views.JobPostingList.as_view(), name="home"),
    path(
        '<int:pk>/', views.JobPostingDetail.as_view(), name="job-post-detail"),
    path('create-job-post/', views.CreateJobPosting.as_view(),
         name="create-job-post"),
    path('update-job-post/<int:pk>', views.UpdateJobPosting.as_view(),
         name='update-job-post'),
    path('delete-job-post/<int:jobpost_id>', views.delete_job_posting,
         name='delete-job-post'),
]

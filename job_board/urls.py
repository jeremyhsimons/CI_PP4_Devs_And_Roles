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
    path('report-job-post/<int:jobpost_id>', views.report_job_posting,
         name='report-job-post'),
    path('application-detail/<int:pk>',
         views.ViewApplicationDetails.as_view(),
         name='application-detail'),
    path('apply/<int:job_id>', views.CreateJobApplication.as_view(),
         name='apply'),
    path('delete_application/<int:application_id>', views.delete_application,
         name='delete_application'),
]

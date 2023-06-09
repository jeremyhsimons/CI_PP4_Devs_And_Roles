from django.urls import path
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from . import views


urlpatterns = [
    path('add_user_profile_details/', views.AddUserProfileDetails.as_view(),
         name='add_user_profile_details'),
    path('redirect/', views.redirect_view, name="redirect"),
    path('see_all_profiles/', views.SeeAllProfiles.as_view(), name="see_all"),
    path('profile_details/<int:pk>', views.ProfileDetail.as_view(),
         name='profile_detail'),
    path('view_profile/', views.ViewProfile.as_view(), name="view_profile"),
    path('edit_profile/', views.EditUserProfileDetails.as_view(),
         name='edit_profile'),
    path('delete_profile/', views.DeleteProfile.as_view(),
         name='delete_profile'),
    path('report_profile/<int:pk>', views.report_profile,
         name='report_profile'),
]

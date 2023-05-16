from django.urls import path
from . import views


urlpatterns = [

    path('add_user_profile_details/', views.AddUserProfileDetails.as_view(),
         name='add_user_profile_details'),
    path('redirect/', views.redirect_view, name="redirect"),
    path('see_all_profiles/', views.SeeAllProfiles.as_view(), name="see_all")
]

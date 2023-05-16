from . import views
from django.urls import path

urlpatterns = [
    path('contact/', views.CreateContactMessage.as_view(), name='contact'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.member_list, name='member_list'),  # Example: List of members
    path('attendance/', views.member_list, name='attendance_list'),  # Example: List of attendance records
    path('membership-types/', views.member_list, name='membership_type_list'),  # Example: List of membership types
]

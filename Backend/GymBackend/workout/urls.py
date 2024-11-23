from django.urls import path
from . import views

urlpatterns = [
    path('trainers/', views.admin_list, name='trainer_list'),  # Example: List of trainers
    path('workout-plans/', views.admin_list, name='workout_plan_list'),  # Example: List of workout plans
    path('workouts/', views.admin_list, name='workout_list'),  # Example: List of workouts
    path('trainer-schedules/', views.admin_list, name='trainer_schedule_list'),  # Example: List of trainer schedules
]

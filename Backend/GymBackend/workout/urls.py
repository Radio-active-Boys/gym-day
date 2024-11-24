from django.urls import path
from .views import (
    TrainerList,
    TrainerDetail,
    WorkoutPlanList,
    WorkoutPlanDetail,
    WorkoutList,
    WorkoutDetail,
    TrainerScheduleList,
    TrainerScheduleDetail,
)

urlpatterns = [

    # Trainers
    path('trainers/', TrainerList.as_view(), name='trainer_list'),
    path('trainers/<str:pk>/', TrainerDetail.as_view(), name='trainer_detail'),

    # Workout Plans
    path('workout-plans/', WorkoutPlanList.as_view(), name='workout_plan_list'),
    path('workout-plans/<str:pk>/', WorkoutPlanDetail.as_view(), name='workout_plan_detail'),

    # Workouts
    path('workouts/', WorkoutList.as_view(), name='workout_list'),
    path('workouts/<str:pk>/', WorkoutDetail.as_view(), name='workout_detail'),

    # Trainer Schedules
    path('trainer-schedules/', TrainerScheduleList.as_view(), name='trainer_schedule_list'),
    path('trainer-schedules/<str:pk>/', TrainerScheduleDetail.as_view(), name='trainer_schedule_detail'),
]

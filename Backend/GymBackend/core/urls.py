from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_list, name='admin_list'),  # Example: List of admins
    path('equipment/', views.admin_list, name='equipment_list'),  # Example: List of equipment
    path('maintenance/', views.admin_list, name='maintenance_list'),  # Example: List of maintenance tasks
]

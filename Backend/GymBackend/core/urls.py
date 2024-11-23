"""from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_list, name='admin_list'),  # Example: List of admins
    path('equipment/', views.admin_list, name='equipment_list'),  # Example: List of equipment
    path('maintenance/', views.admin_list, name='maintenance_list'),  # Example: List of maintenance tasks
]
"""
from django.urls import path
from .views import AdminList, AdminDetail, EquipmentList, EquipmentDetail, MaintenanceList, MaintenanceDetail

urlpatterns = [
    path('admins/', AdminList.as_view(), name='admin_list'),
    path('admins/<int:pk>/', AdminDetail.as_view(), name='admin_detail'),
    path('equipment/', EquipmentList.as_view(), name='equipment_list'),
    path('equipment/<int:pk>/', EquipmentDetail.as_view(), name='equipment_detail'),
    path('maintenance/', MaintenanceList.as_view(), name='maintenance_list'),
    path('maintenance/<int:pk>/', MaintenanceDetail.as_view(), name='maintenance_detail'),
]


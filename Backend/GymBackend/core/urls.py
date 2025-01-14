from django.urls import path
from .views import AdminList, AdminDetail, EquipmentList, EquipmentDetail, MaintenanceList, MaintenanceDetail

urlpatterns = [
    path('admins/', AdminList.as_view(), name='admin_list'),
    path('admins/<str:pk>/', AdminDetail.as_view(), name='admin_detail'),
    path('equipment/', EquipmentList.as_view(), name='equipment_list'),
    path('equipment/<str:pk>/', EquipmentDetail.as_view(), name='equipment_detail'),
    path('maintenance/', MaintenanceList.as_view(), name='maintenance_list'),
    path('maintenance/<str:pk>/', MaintenanceDetail.as_view(), name='maintenance_detail'),
]


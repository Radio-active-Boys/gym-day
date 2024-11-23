from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.admin_list, name='payment_list'),  # Example: List of payments
]

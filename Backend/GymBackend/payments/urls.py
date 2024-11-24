from django.urls import path
from . import views

urlpatterns = [
    # List payments
    path('payments/', views.PaymentListView.as_view(), name='payment-list'),
]

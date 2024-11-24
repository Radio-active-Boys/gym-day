from django.urls import path
from .views import process_payment

urlpatterns = [
    path('', process_payment, name='payment')
]


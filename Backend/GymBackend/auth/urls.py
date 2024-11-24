from django.urls import path
from . import views

urlpatterns = [
    path('create-account/', views.create_account, name='create_account'),
    path('login/', views.login, name='login'),
    path('password-reset/', views.password_reset, name='password_reset'),
]

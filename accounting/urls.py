from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
]

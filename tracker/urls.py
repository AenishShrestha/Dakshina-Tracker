from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_dakshina, name='add_dakshina'),
    path('edit/<int:pk>/', views.edit_dakshina, name='edit_dakshina'),
    path('delete/<int:pk>/', views.delete_dakshina, name='delete_dakshina'),
]
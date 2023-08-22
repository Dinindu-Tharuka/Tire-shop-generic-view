from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeList.as_view()),
    path('services/', views.ServiceList.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('services/<int:pk>/', views.ServiceDetail.as_view()),
]
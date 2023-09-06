from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>/', views.CustomerDetail.as_view()),
    path('vehicles/', views.VehicleList.as_view()),
    path('vehicles/<str:pk>/', views.VehicleDetails.as_view()),
   
]
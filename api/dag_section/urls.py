from django.urls import path
from . import views

urlpatterns = [
    path('taken-tyres-list/', views.TyreTakenListView.as_view()),
    path('customer-taken-tyres-list/', views.CustomerTakenTyresList.as_view()),
    path('taken-tyres-list/<str:pk>/', views.TyreTakenDetailView.as_view()),
    path('send-tyres-list/', views.SendTyreListView.as_view()),
    path('send-tyres-list/<str:pk>/', views.SendTyreDetailView.as_view()),
]
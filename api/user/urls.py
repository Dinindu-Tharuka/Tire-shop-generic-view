from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('user/<str:pk>/', views.UserDetailView.as_view()),
    path('user-profiles/', views.UserProfileListView.as_view()),
    path('user-profiles/<str:pk>/', views.UserProfileDetailView.as_view()),
]
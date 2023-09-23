from django.urls import path
from . import views

urlpatterns = [
    path('taken-tyres-list/', views.TyreTakenListView.as_view()),
    path('taken-tyres-detail/', views.TyreTakenDetailView.as_view()),
]
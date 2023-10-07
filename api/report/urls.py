from django.urls import path
from . import views

urlpatterns = [
    path('rebuild-reports/', views.RebuildReportListView.as_view()),
    path('rebuild-reports/<int:pk>/', views.RebuildReportDetailView.as_view()),
]
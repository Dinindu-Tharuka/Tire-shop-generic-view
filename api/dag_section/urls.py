from django.urls import path
from . import views

urlpatterns = [
    path('taken-tyres-list/', views.TyreTakenListView.as_view()),
    path('customer-taken-tyres-list/', views.CustomerTakenTyresList.as_view()),
    path('taken-tyres-list/<str:pk>/', views.TyreTakenDetailView.as_view()),
    path('send-tyres-list/', views.SendTyreListView.as_view()),
    path('all-send-tyres-list/', views.AllSendTyreList.as_view()),
    path('all-send-supplier-tyres-list/', views.AllSendSupplierTyres.as_view()),
    path('send-tyres-list/<str:pk>/', views.SendTyreDetailView.as_view()),
    path('received-tyres-list/', views.ReceiveTyreListView.as_view()),
    path('received-all-tyres-list/', views.AllReceivedTyres.as_view()),
    path('received-all-supplier-tyres-list/', views.AllReceivedSupplierTyres.as_view()),
    path('received-tyres-list/<str:pk>/',views.ReceiveTyreListDetailView.as_view()),
]

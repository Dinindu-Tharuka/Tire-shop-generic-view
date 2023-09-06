from django.urls import path
from . import views

urlpatterns = [
    path('stock-item-list/', views.StockItemList.as_view()),
    path('stock-item-list/<int:pk>/', views.StockItemDetail.as_view()),
    path('stock-items-invoices/', views.StockItemsInvoiceList.as_view()),
    path('stock-items-invoices/<str:pk>/', views.StockItemsInvoiceDetail.as_view()),
]
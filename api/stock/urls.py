from django.urls import path
from . import views

urlpatterns = [
    path('stock-item-list/', views.StockItemList.as_view()),
    path('stock-item-page-list/', views.StockPageItemList.as_view()),
    path('stock-item-unique-list/', views.StockItemUniqueList.as_view()),
    path('stock-item-list/<int:pk>/', views.StockItemDetail.as_view()),
    path('stock-items-invoices/', views.StockItemsInvoiceList.as_view()),
    path('all-stock-items-invoices/', views.AllStockItemsInvoiceList.as_view()),
    path('stock-items-invoices/<str:pk>/', views.StockItemsInvoiceDetail.as_view()),
    path('stock-payment-list/', views.StockPaymentList.as_view()),
    path('stock-payment-list/<str:pk>/', views.StockPaymentDetail.as_view()),
    path('stock-payments-vouchers/', views.VoucherList.as_view())
]
from django.urls import path
from . import views

urlpatterns = [
    path('bills/', views.BillListView.as_view()),
    path('bills/<str:pk>/', views.BillDetailView.as_view()),
    path('bill-items/', views.BillItemsListView.as_view()),
    path('bill-items/<int:pk>/', views.BillItemsDetailView.as_view()),
    path('bill-service/', views.BillServisesListView.as_view()),
    path('bill-service/<int:pk>/', views.BillServisesDetailView.as_view()),
    path('bill-payments/', views.BillPaymentListView.as_view()),
    path('bill-payments/<int:pk>/', views.BillPaymentDetailView.as_view()),
    path('payments-cash/', views.PaymentCashListView.as_view()),
    path('payments-cash/<int:pk>/', views.PaymentCashDetailView.as_view()),
    path('payments-cheque/', views.PaymentChequeListView.as_view()),
    path('payments-cheque/<int:pk>/', views.PaymentChequeDetailView.as_view()),
    path('payments-credit-card/', views.PaymentCreditCardListView.as_view()),
    path('payments-credit-card/<int:pk>/', views.PaymentCreditCardDetailView.as_view()),
    path('payments-credit/', views.PaymentCreditListView.as_view()),
    path('payments-credit/<int:pk>/', views.PaymentCreditDetailView.as_view()),
]

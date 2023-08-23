from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from billing_data.models import Bill, BillItems, BillServises, BillPayment
from .serializers import BillSerializer, BillItemsSerializer, BillServicesSerilizer, BillPaymentSerializer
from billing_data.models import PaymentCash, PaymentCheque, PaymentCreditCard, PaymentCredit
from .serializers import PaymentCashSerializer, PaymentChequeSerializer, PaymentCreditCardSerializer, PaymentCreditSerializer


class BillListView(ListCreateAPIView):
    queryset = Bill.objects.order_by('-date').all()
    serializer_class = BillSerializer    


class BillDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.order_by('-date').all()
    serializer_class = BillSerializer    


class BillItemsListView(ListCreateAPIView):
    queryset = BillItems.objects.all()
    serializer_class = BillItemsSerializer    


class BillItemsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = BillItems.objects.all()
    serializer_class = BillItemsSerializer    


class BillServisesListView(ListCreateAPIView):
    queryset = BillServises.objects.all()
    serializer_class = BillServicesSerilizer    


class BillServisesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = BillServises.objects.all()
    serializer_class = BillServicesSerilizer   


class BillPaymentListView(ListCreateAPIView):
    queryset = BillPayment.objects.all()
    serializer_class = BillPaymentSerializer    


class BillPaymentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = BillPayment.objects.all()
    serializer_class = BillPaymentSerializer


class PaymentCashListView(ListCreateAPIView):
    queryset = PaymentCash.objects.all()
    serializer_class = PaymentCashSerializer   


class PaymentCashDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PaymentCash.objects.all()
    serializer_class = PaymentCashSerializer    


class PaymentChequeListView(ListCreateAPIView):
    queryset = PaymentCheque.objects.all()
    serializer_class = PaymentChequeSerializer
    

class PaymentChequeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PaymentCheque.objects.all()
    serializer_class = PaymentChequeSerializer    


class PaymentCreditCardListView(ListCreateAPIView):
    queryset = PaymentCreditCard.objects.all()
    serializer_class = PaymentCreditCardSerializer    


class PaymentCreditCardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PaymentCreditCard.objects.all()
    serializer_class = PaymentCreditCardSerializer
   


class PaymentCreditListView(ListCreateAPIView):
    queryset = PaymentCredit.objects.all()
    serializer_class = PaymentCreditSerializer
    


class PaymentCreditDetailView(RetrieveUpdateDestroyAPIView):
    queryset  = PaymentCredit.objects.all()
    serializer_class = PaymentCreditSerializer

    

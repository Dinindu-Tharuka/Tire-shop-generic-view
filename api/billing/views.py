from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from billing_data.models import Bill, BillItems, BillServises, BillPayment
from billing_data.models import PaymentCash, PaymentCheque, PaymentCreditCard, PaymentCredit
from api.paginations import DefaultPagination
from stock_data.models import StockItem
from .serializers import BillSerializer, BillItemsSerializer, BillServicesSerilizer, BillPaymentSerializer
from .serializers import PaymentCashSerializer, PaymentChequeSerializer, PaymentCreditCardSerializer, PaymentCreditSerializer


class BillListView(ListCreateAPIView):
    queryset = Bill.objects \
                    .prefetch_related('bill_items') \
                    .prefetch_related('bill_services') \
                    .prefetch_related('bill_payments') \
                    .prefetch_related('bill_payments__payments_cash') \
                    .prefetch_related('bill_payments__payment_cheques') \
                    .prefetch_related('bill_payments__payments_credit_card') \
                    .prefetch_related('bill_payments__payments_credit') \
                    .order_by('-date').all()
    serializer_class = BillSerializer    
    pagination_class = DefaultPagination


class BillDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects \
                    .prefetch_related('bill_items') \
                    .prefetch_related('bill_services') \
                    .prefetch_related('bill_payments') \
                    .prefetch_related('bill_payments__payments_cash') \
                    .prefetch_related('bill_payments__payment_cheques') \
                    .prefetch_related('bill_payments__payments_credit_card') \
                    .prefetch_related('bill_payments__payments_credit') \
                    .order_by('-date').all()
    serializer_class = BillSerializer    

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        
        print('bill items',instance.bill_items)
        # StockItem.objects.update()

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class BillItemsListView(ListCreateAPIView):
    queryset = BillItems.objects.all()
    serializer_class = BillItemsSerializer    

    


class BillItemsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = BillItems.objects.all()
    serializer_class = BillItemsSerializer  

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        print('items', instance)
        return super().delete(request, *args, **kwargs)  


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

    

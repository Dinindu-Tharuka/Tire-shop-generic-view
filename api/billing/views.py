
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from billing_data.models import Bill, BillItems, BillServises, BillPayment
from billing_data.models import PaymentCash, PaymentCheque, PaymentCreditCard, PaymentCredit
from api.paginations import DefaultPagination
from stock_data.models import StockItem, StockItemUnique
from billing_data.models import DagInvoicePayment
from .serializers import BillSerializer, BillItemsSerializer, BillServicesSerilizer, BillPaymentSerializer
from .serializers import PaymentCashSerializer, PaymentChequeSerializer, PaymentCreditCardSerializer, PaymentCreditSerializer
from .serializers import DagInvoicePaymentSerializer


class BillListView(ListCreateAPIView):
    serializer_class = BillSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        billIdFilter = self.request.GET.get('billIdFilter')
        queryCustomer = self.request.GET.get('billFilterCustomer')
        billVehicleFilter = self.request.GET.get('billVehicleFilter')
        billStartDateFilter = self.request.GET.get('billStartDateFilter')
        billEndDateFilter = self.request.GET.get('billEndDateFilter')

        
        
        if billIdFilter or queryCustomer or billVehicleFilter or billStartDateFilter or billEndDateFilter:
            queryset = Bill.objects \
                .prefetch_related('bill_items') \
                .prefetch_related('bill_services') \
                .prefetch_related('bill_payments') \
                .prefetch_related('bill_payments__payments_cash') \
                .prefetch_related('bill_payments__payment_cheques') \
                .prefetch_related('bill_payments__payments_credit_card') \
                .prefetch_related('bill_payments__payments_credit') \
                .order_by('-date').all()
            if billIdFilter:
                queryset = queryset.filter(invoice_id__startswith=billIdFilter)
            if queryCustomer:
                queryset = queryset.filter(customer__name__startswith=queryCustomer)
            if billVehicleFilter:
                queryset = queryset.filter(vehicle__vehical_no__startswith=billVehicleFilter)
           
        else:
            queryset = Bill.objects \
                .prefetch_related('bill_items') \
                .prefetch_related('bill_services') \
                .prefetch_related('bill_payments') \
                .prefetch_related('bill_payments__payments_cash') \
                .prefetch_related('bill_payments__payment_cheques') \
                .prefetch_related('bill_payments__payments_credit_card') \
                .prefetch_related('bill_payments__payments_credit') \
                .order_by('-date').all()
        return queryset


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
        bill_items = BillItems.objects.filter(bill=instance.invoice_id).all()

        for bill_item in bill_items:
            item_in_stock = bill_item.item
            unit_price = bill_item.customer_unit_price
            remove_item_count = bill_item.qty
            try:
                stock_item_unique = StockItemUnique.objects.get(
                    item=item_in_stock, unit_price=unit_price)
                stock_item_unique.total_qty += remove_item_count
                stock_item_unique.save()
                stock_items = StockItem.objects.filter(
                    stock_item_unique__id=stock_item_unique.id).all()
                for stock_item in stock_items:
                    if stock_item.max_qty >= remove_item_count:
                        stock_item.qty = stock_item.qty + remove_item_count
                        stock_item.save()
                        break
                    else:
                        stock_item.qty = stock_item.qty + stock_item.max_qty
                        remove_item_count = remove_item_count - stock_item.max_qty
                        stock_item.save()
            except:
                pass

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


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
    queryset = PaymentCredit.objects.all()
    serializer_class = PaymentCreditSerializer


class AllDagPaymentsView(ListCreateAPIView):
    queryset = DagInvoicePayment.objects.all()
    serializer_class = DagInvoicePaymentSerializer

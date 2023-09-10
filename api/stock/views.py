from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from stock_data.models import StockItem, StockItemsInvoice
from billing_data.models import BillItems
from api.paginations import DefaultPagination
from .serializers import StockItemDefaultSerializer, StockItemsInvoiceSerilizer


class StockItemList(ListCreateAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockItemDefaultSerializer


class StockItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockItemDefaultSerializer


class StockItemsInvoiceList(ListCreateAPIView):
    serializer_class = StockItemsInvoiceSerilizer
    pagination_class = DefaultPagination

    def get_queryset(self):
        query= self.request.GET.get('invoiceIdFilter')
        queryset = StockItemsInvoice.objects.order_by('-date').filter(invoice_no__startswith=query)
        return queryset


class StockItemsInvoiceDetail(RetrieveUpdateDestroyAPIView):
    queryset = StockItemsInvoice.objects.all()
    serializer_class = StockItemsInvoiceSerilizer

    def delete(self, request, pk):
        stock_ids = StockItem.objects.filter(stock_item_invoice__invoice_no=pk).values('id').distinct()
        if BillItems.objects.filter(stock_item__in = stock_ids).count() > 0:
            return Response({'Error': "you can't delete this invoice. Because it has assosiated Bill items."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        stock_items_invoice = get_object_or_404(StockItemsInvoice, pk=pk)
        stock_items_invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

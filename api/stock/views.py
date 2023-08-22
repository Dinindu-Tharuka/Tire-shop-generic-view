from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from stock_data.models import StockItem, StockItemsInvoice
from .serializers import StockItemSerializer, StockItemsInvoiceSerilizer

class StockItemList(ListCreateAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockItemSerializer
    
    
class StockItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockItemSerializer


class StockItemsInvoiceList(ListCreateAPIView):
    queryset = StockItemsInvoice.objects.all()
    serializer_class = StockItemsInvoiceSerilizer 

    
class StockItemsInvoiceDetail(RetrieveUpdateDestroyAPIView):
    queryset = StockItemsInvoice.objects.all()
    serializer_class = StockItemsInvoiceSerilizer        
    
    def delete(self, request, pk):
        if StockItem.objects.filter(stock_item_invoice__invoice_no = pk).count() > 0:
            return Response({'Error':"you can't delete this invoice. Because it has assosiated items."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        stock_items_invoice = get_object_or_404(StockItemsInvoice, pk=pk)        
        stock_items_invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

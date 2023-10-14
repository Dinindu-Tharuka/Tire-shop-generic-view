from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from stock_data.models import StockItem, StockItemsInvoice, StockItemUnique, StockPayment
from billing_data.models import BillItems
from api.paginations import DefaultPagination
import datetime
from .serializers import StockItemDefaultSerializer, StockItemsInvoiceSerilizer, StockItemUniqueSerializer, StockPaymentSerializer

class ConvertDateToDateTime:
    def __init__(self, date_start=None, date_end=None):
        self.date_start = date_start
        self.date_end = date_end

        if self.date_end and self.date_start:
            date_object_start = datetime.datetime.strptime(self.date_start, "%Y-%m-%d").date()
            date_object_end = datetime.datetime.strptime(self.date_end, "%Y-%m-%d").date()
            self.today_min = datetime.datetime.combine(date_object_start, datetime.time.min)
            self.today_max = datetime.datetime.combine(date_object_end, datetime.time.max)
        elif self.date_start:
            date_object = datetime.datetime.strptime(self.date_start, "%Y-%m-%d").date()
            self.today_min = datetime.datetime.combine(date_object, datetime.time.min)
            self.today_max = datetime.datetime.combine(date_object, datetime.time.max)

    def converted_min(self):
        return self.today_min
    
    def converted_max(self):
        return self.today_max

class StockItemUniqueList(ListCreateAPIView):
    queryset = StockItemUnique.objects.all()
    serializer_class = StockItemUniqueSerializer

class StockItemList(ListAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockItemDefaultSerializer

    def get_queryset(self):
        stockItemsInvoiceNoFilter = self.request.GET.get('stockItemsInvoiceNoFilter')
        stockItemsItemIdFilter = self.request.GET.get('stockItemsItemIdFilter')
        stockItemsBrandFilter = self.request.GET.get('stockItemsBrandFilter')
        stockItemsSizeFilter = self.request.GET.get('stockItemsSizeFilter')
        stockItemsStartDateFilter = self.request.GET.get('stockItemsStartDateFilter')
        stockItemsEndDateFilter = self.request.GET.get('stockItemsEndDateFilter')

        if stockItemsInvoiceNoFilter or stockItemsItemIdFilter or stockItemsBrandFilter or stockItemsSizeFilter or stockItemsStartDateFilter or stockItemsEndDateFilter:
            queryset = StockItem.objects.all()
            if stockItemsInvoiceNoFilter:
                queryset = queryset.filter(stock_invoice__invoice_no__istartswith = stockItemsInvoiceNoFilter)
            if stockItemsItemIdFilter:
                queryset = queryset.filter(item__item_id__istartswith=stockItemsItemIdFilter)
            if stockItemsBrandFilter:
                queryset = queryset.filter(item__brand__istartswith=stockItemsBrandFilter)
            if stockItemsSizeFilter:
                queryset = queryset.filter(item__size__istartswith=stockItemsSizeFilter)
            if stockItemsStartDateFilter or stockItemsEndDateFilter:
                date_object = ConvertDateToDateTime(stockItemsStartDateFilter, stockItemsEndDateFilter)
                queryset = queryset.filter(date__range = (date_object.converted_min(), date_object.converted_max()))                
        else:
            queryset = StockItem.objects.all()
        return queryset
        
    
class StockPageItemList(ListAPIView):    
    serializer_class = StockItemDefaultSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        pageStockItemsInvoiceNoFilter = self.request.GET.get('pageStockItemsInvoiceNoFilter')
        pageStockItemsItemIdFilter = self.request.GET.get('pageStockItemsItemIdFilter')
        pageStockItemsBrandFilter = self.request.GET.get('pageStockItemsBrandFilter')
        pageStockItemsSizeFilter = self.request.GET.get('pageStockItemsSizeFilter')
        pageStockItemsStartDateFilter = self.request.GET.get('pageStockItemsStartDateFilter')
        pageStockItemsEndDateFilter = self.request.GET.get('pageStockItemsEndDateFilter')

        if pageStockItemsInvoiceNoFilter or pageStockItemsItemIdFilter or pageStockItemsBrandFilter or pageStockItemsSizeFilter or pageStockItemsStartDateFilter or pageStockItemsEndDateFilter:
            queryset = StockItem.objects.all()
            if pageStockItemsInvoiceNoFilter:
                queryset = queryset.filter(stock_invoice__invoice_no__istartswith = pageStockItemsInvoiceNoFilter)
            if pageStockItemsItemIdFilter:
                queryset = queryset.filter(item__item_id__istartswith=pageStockItemsItemIdFilter)
            if pageStockItemsBrandFilter:
                queryset = queryset.filter(item__brand__istartswith=pageStockItemsBrandFilter)
            if pageStockItemsSizeFilter:
                queryset = queryset.filter(item__size__istartswith=pageStockItemsSizeFilter)
            if pageStockItemsStartDateFilter or pageStockItemsEndDateFilter:
                date_object = ConvertDateToDateTime(pageStockItemsStartDateFilter, pageStockItemsEndDateFilter)
                queryset = queryset.filter(date__range = (date_object.converted_min(), date_object.converted_max()))                
        else:
            queryset = StockItem.objects.all()
        return queryset

class StockItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockItemDefaultSerializer


class StockItemsInvoiceList(ListCreateAPIView):
    serializer_class = StockItemsInvoiceSerilizer
    pagination_class = DefaultPagination

    def get_queryset(self):
        query= self.request.GET.get('invoiceIdFilter')
        if query:
            queryset = StockItemsInvoice.objects.order_by('-date').filter(invoice_no__startswith=query)
        else:
            queryset = StockItemsInvoice.objects.all()
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

class StockPaymentList(ListCreateAPIView):
    queryset = StockPayment.objects.all()
    serializer_class = StockPaymentSerializer

class StockPaymentDetail(RetrieveUpdateDestroyAPIView):
    queryset = StockPayment.objects.all()
    serializer_class = StockPaymentSerializer
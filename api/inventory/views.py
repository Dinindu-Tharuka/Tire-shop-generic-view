from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from inventory_data.models import ItemCategory, Supplier, Item
from stock_data.models import StockItemsInvoice, StockItem
from .serializers import ItemCategorySerializer, SupplierSerializer, ItemSerializer
from api.paginations import DefaultPagination


class ItemCategoryList(ListCreateAPIView):
    serializer_class = ItemCategorySerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        categoryNameFilterValue = self.request.GET.get('categoryNameFilter')
        if categoryNameFilterValue:
            queryset = ItemCategory.objects.filter(category_name__istartswith=categoryNameFilterValue)
        else:
            queryset = ItemCategory.objects.all()
        return queryset



class ItemCategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer

    def delete(self, request, pk):
        if Item.objects.filter(item_category_id=pk).count() > 0:
            return Response({'Error': "You can't delete this Category, because there are some category associated items."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        customer = get_object_or_404(ItemCategory, pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SupplierAllList(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    
class SupplierList(ListCreateAPIView):
    serializer_class = SupplierSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        supplierFilaterValue = self.request.GET.get('supplierNameFilter')
        if supplierFilaterValue:
            queryset =  Supplier.objects.filter(name__istartswith = supplierFilaterValue)
        else:
            queryset = Supplier.objects.all()
        return queryset


class SupplierDetail(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def delete(self, request, pk):
        if Item.objects.filter(supplier_id=pk).count() or StockItemsInvoice.objects.filter(supplier_id=pk).count() > 0:
            return Response({'Error': "You can't delete this supplier, because there are some supplier associated fields."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        supplier = get_object_or_404(Supplier, pk=pk)
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemListPagination(ListCreateAPIView):
    serializer_class = ItemSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        query_item_id = self.request.GET.get('itemQuery')
        query_size = self.request.GET.get('itemSizeQuery')

        print(query_item_id)
       
        
        queryset = Item.objects.filter(item_id__startswith = query_item_id).filter(size__istartswith= query_size)
        return queryset

class ItemList(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def delete(self, request, pk):
        if StockItem.objects.filter(item_id=pk).count() > 0:
            return Response({"Error": "You can't delete this item because it has associated fields."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

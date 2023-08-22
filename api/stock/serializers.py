from rest_framework import serializers
from stock_data.models import StockItem, StockItemsInvoice
import pprint

class StockItemSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = StockItem
        fields = ['id', 'item', 'retail_price', 'date', 'stock_item_invoice', 'cost', 'selling_price', 'discount', 'qty', 'sold_qty']

class StockItemsInvoiceSerilizer(serializers.ModelSerializer):
    stockitems = StockItemSerializer(many=True)
    date = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = StockItemsInvoice
        fields = ['invoice_no', 'date', 'total_amount', 'total_discount', 'supplier', 'stockitems']

    def create(self, validated_data):
        items = validated_data.pop('stockitems')
        invoice = StockItemsInvoice.objects.create(**validated_data)

        for item in items:
            item.pop('stock_item_invoice')
            StockItem.objects.create(stock_item_invoice=invoice, **item)
        return invoice
    
    def update(self, instance, validated_data):

        
        stockitems_data = validated_data.pop('stockitems')    
    

        # Update the invoice fields
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.total_discount = validated_data.get('total_discount', instance.total_discount)

        # Get record of previous stock items
        previousely_entered_stock_items = [item.item for item in instance.stockitems.all()]        
        instance.save()

        for stockitem_data in stockitems_data:    
            stockitem_data.pop('stock_item_invoice') 
            # Check if available duplicates         
            if stockitem_data.get('item') not in previousely_entered_stock_items:
                StockItem.objects.create(stock_item_invoice=instance, **stockitem_data)
        return instance
from rest_framework import serializers
from stock_data.models import StockItem, StockItemsInvoice, StockItemUnique

class StockItemUniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockItemUnique
        fields = ['id', 'item', 'total_qty', 'unit_price']


class StockItemDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockItem
        fields = ['id', 'stock_invoice', 'stock_item_unique', 'item', 'retail_price', 'cost', 'customer_price', 'supplier_discount', 'sales_discount', 'customer_discount', 'qty', 'customer_unit_price']

class StockItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = StockItem
        fields = ['id', 'item', 'retail_price', 'cost', 'customer_price', 'supplier_discount', 'sales_discount', 'customer_discount', 'qty']

class StockItemsInvoiceSerilizer(serializers.ModelSerializer):
    stock_items = StockItemSerializer(many=True)
    date = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = StockItemsInvoice
        fields = ['invoice_no', 'date', 'total_amount', 'total_discount', 'supplier', 'stock_items']

    def create(self, validated_data):
        items = validated_data.pop('stock_items')
        invoice = StockItemsInvoice.objects.create(**validated_data)
        stock_items = []
        for item in items:
            stock_item = item['item']
            customer_price = item['customer_price']
            qty = item['qty']
            unit_price : float = customer_price/qty
            
            try:
                stock_item_unique = StockItemUnique.objects.get(item__item_id=stock_item, unit_price=unit_price)
                stock_item_unique.total_qty += qty
                stock_item_unique.save()
                StockItem.objects.create(stock_invoice=invoice, stock_item_unique_id=stock_item_unique.id, customer_unit_price=unit_price, max_qty=qty, **item)
                
            except:
                stock_item_unique = StockItemUnique.objects.create(item=stock_item, total_qty=qty, unit_price=unit_price)
                StockItem.objects.create(stock_invoice=invoice, stock_item_unique=stock_item_unique, customer_unit_price=unit_price, max_qty=qty, **item)
                
        invoice.stock_items.set(stock_items)
        return invoice
    
    
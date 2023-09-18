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
    # stock_item_invoice = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = StockItem
        fields = ['id', 'stock_invoice', 'stock_item_unique', 'item', 'retail_price', 'cost', 'customer_price', 'supplier_discount', 'sales_discount', 'customer_discount', 'qty', 'customer_unit_price']

class StockItemsInvoiceSerilizer(serializers.ModelSerializer):
    stock_items = StockItemSerializer(many=True)
    date = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = StockItemsInvoice
        fields = ['invoice_no', 'date', 'total_amount', 'total_discount', 'supplier', 'stock_items']

    def create(self, validated_data):
        items = validated_data.pop('stock_items')
        invoice = StockItemsInvoice.objects.create(**validated_data)

        print('items', items)
        stock_items = []
        for item in items:
            item.pop('stock_invoice')
            item.pop('stock_item_unique')
            stock_item = item['item']
            unit_price = item['customer_unit_price']
            qty = item['qty']
            print('unit_price', unit_price)
            print('qty', qty)
            print('item', stock_item)
            
            try:
                stock_item_unique = StockItemUnique.objects.get(item__item_id=stock_item, unit_price=unit_price)
                stock_item_unique.total_qty += qty
                stock_item_unique.save()
                print('stock unique id', stock_item_unique.id)
                StockItem.objects.create(stock_invoice=invoice, stock_item_unique_id=stock_item_unique.id, **item)
                print('gt item', stock_item_unique)
            except:
                print('Not get item')
                stock_item_unique = StockItemUnique.objects.create(item=stock_item, total_qty=qty, unit_price=unit_price)
                StockItem.objects.create(stock_invoice=invoice, stock_item_unique=stock_item_unique, **item)
                print('created stock unique')
        invoice.stock_items.set(stock_items)
        return invoice
    
    
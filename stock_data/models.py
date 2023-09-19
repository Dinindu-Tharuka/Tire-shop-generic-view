from django.db import models
from inventory_data.models import Item, Supplier

MAX_DIGITS = 8
DECIMAL_PLACES = 2



class StockItemUnique(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)    
    total_qty = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

class StockItemsInvoice(models.Model):
    invoice_no = models.CharField(max_length=20, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_discount = models.DecimalField(max_digits=10, decimal_places=2)

    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.invoice_no

class StockItem(models.Model):     
    stock_invoice = models.ForeignKey(StockItemsInvoice, on_delete=models.CASCADE, related_name='stock_items')
    stock_item_unique = models.ForeignKey(StockItemUnique, on_delete=models.CASCADE, related_name='stock_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    customer_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_discount = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    sales_discount = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    customer_discount = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.PositiveSmallIntegerField()
    customer_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_qty = models.PositiveIntegerField()

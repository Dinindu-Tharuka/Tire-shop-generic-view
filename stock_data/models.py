from django.db import models
from inventory_data.models import Item, Supplier


class StockItemsInvoice(models.Model):
    invoice_no = models.CharField(max_length=20, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    total_discount = models.DecimalField(max_digits=8, decimal_places=2)

    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.invoice_no

class StockItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    stock_item_invoice = models.ForeignKey(StockItemsInvoice, on_delete=models.PROTECT, related_name='stockitems')

    retail_price = models.DecimalField(max_digits=8, decimal_places=2)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    qty = models.PositiveSmallIntegerField()
    sold_qty = models.PositiveSmallIntegerField()

    

from django.db import models
from inventory_data.models import Item, Supplier

MAX_DIGITS = 10
DECIMAL_PLACES = 2


class StockItemUnique(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    total_qty = models.PositiveIntegerField()
    unit_price = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)


class StockItemsInvoice(models.Model):
    invoice_no = models.CharField(max_length=20, primary_key=True)
    bill_invoice_no = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    total_discount = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.invoice_no


class StockItem(models.Model):
    stock_invoice = models.ForeignKey(
        StockItemsInvoice, on_delete=models.CASCADE, related_name='stock_items')
    stock_item_unique = models.ForeignKey(
        StockItemUnique, on_delete=models.CASCADE, related_name='stock_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    retail_price = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    customer_price = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    supplier_discount = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    sales_discount = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    customer_discount = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    qty = models.PositiveSmallIntegerField()
    customer_unit_price = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    max_qty = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)


PAYMENT_SELECT = 'select'
PAYMENT_CASH = 'cash'
PAYMENT_CHEQUE = 'cheque'
PAYMENT_CREDIT_CARD = 'credit_card'


PAYMENT_METHODS = [
    (PAYMENT_SELECT, 'Select'),
    (PAYMENT_CASH, 'Cash'),
    (PAYMENT_CHEQUE, 'Cheque'),
    (PAYMENT_CREDIT_CARD, 'Credit Card'),
]


class Voucher(models.Model):
    voucher = models.CharField(max_length=20, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    total_payment = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)


class StockPayment(models.Model):
    is_cash = models.BooleanField(default=False)
    is_cheque = models.BooleanField(default=False)
    is_credit_card = models.BooleanField(default=False)
    amount = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    date = models.DateTimeField(auto_now_add=True)

    # Cheque Detail
    bank = models.CharField(max_length=50, null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)
    cheque_date = models.DateField(null=True, blank=True)

    # Invoice no
    stock_invoice = models.ForeignKey(
        StockItemsInvoice, on_delete=models.PROTECT, related_name='stock_payments')

    # Voucher
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE,
                                null=True, blank=True, related_name='stock_payments')

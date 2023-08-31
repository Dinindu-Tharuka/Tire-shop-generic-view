from django.db import models
from customer_data.models import Customer
from inventory_data.models import Item
from services_data.models import Service, Employee
from stock_data.models import StockItem



class Bill(models.Model):
    invoice_id = models.CharField(max_length=50, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='bills')
    
    date = models.DateField(auto_now_add=True)
    discount_amount = models.DecimalField(max_digits=8, decimal_places=2)
    sub_total = models.DecimalField(max_digits=8, decimal_places=2)
    custome_item_value = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.invoice_id

class BillItems(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name='items')
    stock_item = models.ForeignKey(StockItem, on_delete=models.PROTECT, related_name='bill_items')
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='bill_items')
    qty = models.PositiveSmallIntegerField()   
    customer_discount = models.DecimalField(max_digits=8, decimal_places=2)    
    customer_price = models.DecimalField(max_digits=8, decimal_places=2)

class BillServises(models.Model):
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='bill_services')
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='bill_services')
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='bill_services')

   

PAYMENT_SELECT = 'select'
PAYMENT_CASH = 'cash'
PAYMENT_CHEQUE = 'cheque'
PAYMENT_CREDIT_CARD = 'credit_card'
PAYMENT_CREDIT = 'credit'
PAYMENT_MULTIPLE = 'multiple'

PAYMENT_METHODS = [
    (PAYMENT_SELECT, 'Select'),
    (PAYMENT_CASH, 'Cash'),
    (PAYMENT_CHEQUE, 'Cheque'),
    (PAYMENT_CREDIT_CARD, 'Credit Card'),
    (PAYMENT_CREDIT, 'Credit'),
    (PAYMENT_MULTIPLE, 'multiple'),
]

class BillPayment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='bill_payments')

    date = models.DateField(auto_now_add=True)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_methods = models.CharField(max_length=20, choices=PAYMENT_METHODS, default=PAYMENT_SELECT)

    def __str__(self) -> str:
        return self.bill.invoice_id
    
    
class PaymentCash(models.Model):
    bill_payment = models.ForeignKey(BillPayment, on_delete=models.CASCADE, related_name='payments_cash')

    date = models.DateField(auto_now_add=True)
    payeename = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

   


class PaymentCheque(models.Model):
    bill_payment = models.ForeignKey(BillPayment, on_delete=models.CASCADE, related_name='payment_cheques')

    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    cheque_no = models.CharField(max_length=50)
    payeename = models.CharField(max_length=50)
    bank = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    cheque_date = models.DateField()

    


class PaymentCreditCard(models.Model):
    bill_payment = models.ForeignKey(BillPayment, on_delete=models.CASCADE, related_name='payments_credit_card')

    date = models.DateField(auto_now_add=True)
    payeename = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    

class PaymentCredit(models.Model):
    bill_payment = models.ForeignKey(BillPayment, on_delete=models.CASCADE, related_name='payments_credit')

    date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    payeename = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    



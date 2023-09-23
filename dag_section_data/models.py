from django.db import models
from customer_data.models import Customer, Vehical
from inventory_data.models import Supplier

# Take part
class TakenTyre(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehical,on_delete=models.CASCADE)
    taken_date = models.DateTimeField(auto_now_add=True)

class CustomerTakenTyre(models.Model):
    rebuild_id = models.CharField(max_length=50, primary_key=True)
    tyre_taken = models.ForeignKey(TakenTyre, on_delete=models.CASCADE, related_name='customer_tyres')
    tyre_no = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)


## Send part
class SendTyre(models.Model):
    order_no = models.CharField(max_length=50, primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    customer_taken_tyre = models.OneToOneField(CustomerTakenTyre, on_delete=models.CASCADE)



REJECTED = 'send'
SELECT = 'select'

STATUS = [
    (REJECTED, 'send'),
    (SELECT, 'Select')
]

class SendSupplierTyre(models.Model):
    job_no = models.CharField(max_length=50, primary_key=True)
    send_tyre = models.ForeignKey(SendTyre, on_delete=models.CASCADE)
    customer_taken_tyre = models.OneToOneField(CustomerTakenTyre, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default=SELECT)


## Received

class ReceivedTyre(models.Model):
    invoice_no = models.CharField(max_length=50, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)

RECEIVED = 'received'
REJECTED = 'rejected'

STATUS_RECEIVED = [
    (RECEIVED, 'received'),
    (REJECTED, 'rejected'),
    (SELECT, 'Select')
]


class ReceivedSupplierTyre(models.Model):
    send_supplier_tyre = models.OneToOneField(SendSupplierTyre, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_RECEIVED, default=SELECT)
    received_tyre = models.ForeignKey(ReceivedTyre, on_delete=models.CASCADE)
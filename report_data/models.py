from django.db import models
from dag_section_data.models import CustomerTakenTyre
from customer_data.models import Customer, Vehical
from inventory_data.models import Supplier


class RebuildReport(models.Model):
    rebuild_id = models.OneToOneField(CustomerTakenTyre, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehical, on_delete=models.CASCADE)
    taken_date = models.CharField(max_length=100)
    tyre_no = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    send_date = models.CharField(max_length=100, null=True, blank=True)
    order_no = models.CharField(max_length=50, null=True, blank=True)
    job_no = models.CharField(max_length=50, null=True, blank=True)

    status = models.CharField(max_length=20, null=True, blank=True)
    invoice_date = models.CharField(max_length=100, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

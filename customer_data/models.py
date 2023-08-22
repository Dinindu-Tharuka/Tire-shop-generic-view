from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    telephone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return self.name

class Vehical(models.Model):
    vehical_no = models.CharField(primary_key=True, max_length=50)
    type = models.CharField(max_length=50)
    madal =models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.vehical_no
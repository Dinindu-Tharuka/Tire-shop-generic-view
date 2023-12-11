from django.db import models

class Employee(models.Model):
    nic = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    address = models.TextField()
    telephone = models.CharField(max_length=15)
    designation = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Service(models.Model):
    description = models.TextField()
    service_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.description



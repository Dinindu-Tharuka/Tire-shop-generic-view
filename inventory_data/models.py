from django.db import models


class ItemCategory(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.category_name

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    telephone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name

LONG_VALVE = 'Long Valve'
SHORT_VALVE = 'Short Valve'
SELECT = 'Not selected'

VALE_CHOICES = [
    (LONG_VALVE, 'Long Valve'),
    (SHORT_VALVE, 'Short Valve'),
    (SELECT, 'Select')
]


class Item(models.Model):
    item_id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    brand = models.CharField(max_length=20, null=True, blank=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    plyrating = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    vale_type = models.CharField(max_length=20, choices=VALE_CHOICES, default=SELECT)

    item_category = models.ForeignKey(ItemCategory, on_delete=models.PROTECT, related_name='items', null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='items', null=True, blank=True)

    def __str__(self) -> str:
        return self.item_id




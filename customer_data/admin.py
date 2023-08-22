from django.contrib import admin
from .models import Customer, Vehical

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Vehical)
class VehicalAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import TakenTyre, CustomerTakenTyre

@admin.register(TakenTyre)
class TakenTyreAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomerTakenTyre)
class CustomerTakenTyreAdmin(CustomerTakenTyre):
    pass

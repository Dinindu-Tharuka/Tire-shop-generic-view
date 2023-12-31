from django.contrib import admin
from .models import TakenTyre, CustomerTakenTyre
from .models import SendTyre, SendSupplierTyre
from .models import ReceivedTyre, ReceivedSupplierTyre

# Taken tyre
@admin.register(TakenTyre)
class TakenTyreAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomerTakenTyre)
class CustomerTakenTyreAdmin(admin.ModelAdmin):
    pass

# Send Tyre
@admin.register(SendTyre)
class SendTyreAdmin(admin.ModelAdmin):
    pass

@admin.register(SendSupplierTyre)
class SendSupplierTyreAdmin(admin.ModelAdmin):
    pass

@admin.register(ReceivedTyre)
class ReceivedTyreAdmin(admin.ModelAdmin):
    pass

@admin.register(ReceivedSupplierTyre)
class ReceivedSupplierTyreAdmin(admin.ModelAdmin):
    pass
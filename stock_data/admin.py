from django.contrib import admin
from .models import StockItem, StockItemsInvoice, StockItemUnique

@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    pass

@admin.register(StockItemsInvoice)
class StockItemsInvoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(StockItemUnique)
class StockItemUniqueAdmin(admin.ModelAdmin):
    pass




from django.contrib import admin
from .models import StockItem, StockItemsInvoice

@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    pass

class StockItemInline(admin.TabularInline):
    model = StockItem
    extra = 1
    
@admin.register(StockItemsInvoice)
class StockItemsInvoiceAdmin(admin.ModelAdmin):
    inlines = [StockItemInline]




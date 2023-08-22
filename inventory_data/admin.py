from django.contrib import admin
from .models import Item, ItemCategory, Supplier

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass

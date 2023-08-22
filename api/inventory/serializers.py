from rest_framework import serializers
from inventory_data.models import ItemCategory, Supplier, Item

class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ['id', 'category_name', 'description']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'address', 'telephone', 'mobile', 'email']

class ItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Item
        fields = ['item_id', 'name', 'size', 'brand', 'type', 'plyrating', 'country', 'vale_type', 'item_category', 'supplier']
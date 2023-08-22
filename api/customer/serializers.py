from rest_framework import serializers
from customer_data.models import Customer, Vehical

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'telephone', 'mobile', 'email']

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehical
        fields = ['vehical_no', 'type', 'madal', 'brand', 'customer']
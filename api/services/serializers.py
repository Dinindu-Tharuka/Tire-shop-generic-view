from rest_framework import serializers
from services_data.models import Employee, Service

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'nic', 'name', 'address', 'telephone', 'designation']

class ServicesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'description', 'service_value']
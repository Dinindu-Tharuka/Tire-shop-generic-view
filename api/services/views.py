from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from services_data.models import Employee, Service
from .serializers import EmployeeSerializer, ServicesSerilizer



class EmployeeList(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    


class ServiceList(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerilizer
    
    
class ServiceDetail(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerilizer
    
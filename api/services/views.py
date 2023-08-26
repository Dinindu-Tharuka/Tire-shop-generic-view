from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from services_data.models import Employee, Service
from api.paginations import DefaultPagination
from .serializers import EmployeeSerializer, ServicesSerilizer



class EmployeeList(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = DefaultPagination
    
    
class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    


class ServiceList(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerilizer
    pagination_class = DefaultPagination
    
    
class ServiceDetail(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerilizer
    
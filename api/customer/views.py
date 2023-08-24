from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from customer_data.models import Customer, Vehical
from billing_data.models import Bill
from .serializers import CustomerSerializer, VehicleSerializer
from rest_framework.pagination import PageNumberPagination

class pagenumber(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 7

class CustomerList(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer   
    pagination_class = pagenumber 


class CustomerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def delete(self, request, pk):
        if Bill.objects.filter(customer_id=pk).count() > 0:
            return Response({'Error': "You can't delete this customer. Because thiscustomer has associted Bills."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
          
    

    
class VehicleList(ListCreateAPIView):
    queryset = Vehical.objects.all()
    serializer_class = VehicleSerializer
    
    
class VehicleDetails(RetrieveUpdateDestroyAPIView):
    queryset = Vehical.objects.all()
    serializer_class = VehicleSerializer
    
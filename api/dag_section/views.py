from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from dag_section_data.models import TakenTyre, CustomerTakenTyre
from dag_section_data.models import SendTyre, SendSupplierTyre
from .serializers import TakenTyreUpdateSerializer, TakenTyreCreateSerializer, CustomerTakenTyreSerializer
from .serializers import SendTyreCreateSerializer, SendTyreUpdateSerializer
from api.paginations import DefaultPagination

class CustomerTakenTyresList(ListCreateAPIView):
    queryset = CustomerTakenTyre.objects.order_by('-tyre_taken__taken_date').all()
    serializer_class = CustomerTakenTyreSerializer


class TyreTakenListView(ListCreateAPIView):
    queryset = TakenTyre.objects.order_by('-taken_date').all()
    serializer_class = TakenTyreCreateSerializer
    pagination_class = DefaultPagination


class TyreTakenDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TakenTyre.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TakenTyreCreateSerializer
        return TakenTyreUpdateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        customer_tyres = request.data.get('customer_tyres')
        
        for tyre in customer_tyres:
            try:
                CustomerTakenTyre.objects.get(rebuild_id=tyre['rebuild_id'])
            except:
                CustomerTakenTyre.objects.create(**tyre, tyre_taken=instance)
        return super().update(request, *args, **kwargs)


class SendTyreListView(ListCreateAPIView):
    queryset = SendTyre.objects.order_by('-taken_date').all()
    serializer_class = SendTyreCreateSerializer
    pagination_class = DefaultPagination


class SendTyreDetailView(RetrieveUpdateDestroyAPIView):
    queryset = SendTyre.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SendTyreCreateSerializer
        return SendTyreUpdateSerializer    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance.send_tyres.all(), 'instance')
        supplier_tyres = request.data.get('send_tyres')

        print(supplier_tyres, 'supplier_tyres')
        for saved_tyre in instance.send_tyres.all():
            for tyre in supplier_tyres:
                if saved_tyre.job_no == tyre['job_no']:
                    print(1)
                    break
            else:
                try:
                    sendTyre = SendSupplierTyre.objects.get(job_no=saved_tyre.job_no)
                    sendTyre.delete()
                except:
                    pass
                    

        for tyre in supplier_tyres:           
            try:
                SendSupplierTyre.objects.get(job_no=tyre['job_no'])
            except:
                customer_taken_tyre_id = tyre.pop('customer_taken_tyre')
                customer_taken_tyre_instance = CustomerTakenTyre.objects.get(rebuild_id=customer_taken_tyre_id)
                SendSupplierTyre.objects.create(send_tyre=instance, customer_taken_tyre=customer_taken_tyre_instance, **tyre)
                
        return super().update(request, *args, **kwargs)

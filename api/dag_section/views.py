from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from dag_section_data.models import TakenTyre, CustomerTakenTyre
from dag_section_data.models import SendTyre, SendSupplierTyre
from .serializers import TakenTyreUpdateSerializer, TakenTyreCreateSerializer
from .serializers import SendTyreCreateSerializer, SendTyreUpdateSerializer
from api.paginations import DefaultPagination


class TyreTakenListView(ListCreateAPIView):
    queryset = TakenTyre.objects.all()
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
    queryset = SendTyre.objects.all()
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
        supplier_tyres = request.data.get('send_tyres')
        for tyre in supplier_tyres:
            try:
                SendSupplierTyre.objects.get(job_no=tyre['job_no'])
            except:
                customer_taken_tyre_id = tyre.pop('customer_taken_tyre')
                customer_taken_tyre_instance = CustomerTakenTyre.objects.get(rebuild_id=customer_taken_tyre_id)
                SendSupplierTyre.objects.create(send_tyre=instance, customer_taken_tyre=customer_taken_tyre_instance, **tyre)
                
        return super().update(request, *args, **kwargs)

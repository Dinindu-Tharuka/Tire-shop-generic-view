from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from dag_section_data.models import TakenTyre, CustomerTakenTyre
from .serializers import TakenTyreUpdateSerializer, TakenTyreCreateSerializer
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

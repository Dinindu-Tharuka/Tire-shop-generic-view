from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from dag_section_data.models import TakenTyre
from .serializers import TakenTyreSerializer


class TyreTakenListView(ListCreateAPIView):
    queryset = TakenTyre
    serializer_class = TakenTyreSerializer

class TyreTakenDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TakenTyre
    serializer_class = TakenTyreSerializer


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from dag_section_data.models import TakenTyre, CustomerTakenTyre
from dag_section_data.models import SendTyre, SendSupplierTyre
from dag_section_data.models import ReceivedTyre, ReceivedSupplierTyre
from .serializers import TakenTyreUpdateSerializer, TakenTyreCreateSerializer, CustomerTakenTyreSerializer
from .serializers import SendTyreCreateSerializer, SendTyreUpdateSerializer, SendSupplierTyreSerializer
from .serializers import ReceivedTyreSerializer, ReceivedTyreUpdateSerializer, ReceivedSupplierTyreSerializer
from api.paginations import DefaultPagination
from report_data.models import RebuildReport


class CustomerTakenTyresList(ListCreateAPIView):
    queryset = CustomerTakenTyre.objects.order_by(
        '-tyre_taken__taken_date').all()
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

    def delete(self, request, *args, **kwargs):
        taken_tyre_instance = self.get_object()

        for customer_tyre in taken_tyre_instance.customer_tyres.all():
            rebuild_id = customer_tyre.rebuild_id
            try:
                rebuild_report = RebuildReport.objects.get(
                    rebuild_id=rebuild_id)
                rebuild_report.delete()
                print('entry deleted')
            except:
                print('there is no entry of report.')

        return super().delete(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        customer_tyres = request.data.get('customer_tyres')

        for saved_tyre in instance.customer_tyres.all():
            for tyre in customer_tyres:
                if saved_tyre.rebuild_id == tyre['rebuild_id']:
                    break
            else:
                customer_tyre = CustomerTakenTyre.objects.get(
                    rebuild_id=saved_tyre.rebuild_id)
                customer_tyre.delete()

        for tyre in customer_tyres:
            try:
                CustomerTakenTyre.objects.get(rebuild_id=tyre['rebuild_id'])
            except:
                customer_taken_tyre = CustomerTakenTyre.objects.create(
                    **tyre, tyre_taken=instance)
                                
                # Report
                RebuildReport.objects.create(
                    rebuild_id=customer_taken_tyre,
                    customer_id=instance.customer.id,
                    vehicle_id=instance.vehicle.vehical_no,
                    taken_date=instance.taken_date,
                    tyre_no=customer_taken_tyre.tyre_no,
                    size=customer_taken_tyre.size,
                    brand=customer_taken_tyre.brand
                )  
                print('updated')             

        return super().update(request, *args, **kwargs)


class AllSendSupplierTyres(ListCreateAPIView):
    queryset = SendSupplierTyre.objects.all()
    serializer_class = SendSupplierTyreSerializer


class AllSendTyreList(ListCreateAPIView):
    queryset = SendTyre.objects.all()
    serializer_class = SendTyreCreateSerializer


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
        supplier_tyres = request.data.get('send_tyres')
        for saved_tyre in instance.send_tyres.all():
            for tyre in supplier_tyres:
                if saved_tyre.job_no == tyre['job_no']:
                    break
            else:
                try:
                    sendTyre = SendSupplierTyre.objects.get(
                        job_no=saved_tyre.job_no)
                    sendTyre.delete()
                except:
                    pass

        for tyre in supplier_tyres:
            try:
                SendSupplierTyre.objects.get(job_no=tyre['job_no'])
            except:
                customer_taken_tyre_id = tyre.pop('customer_taken_tyre')
                customer_taken_tyre_instance = CustomerTakenTyre.objects.get(
                    rebuild_id=customer_taken_tyre_id)
                SendSupplierTyre.objects.create(
                    send_tyre=instance, customer_taken_tyre=customer_taken_tyre_instance, **tyre)

        return super().update(request, *args, **kwargs)


# Received Tyre

class AllReceivedTyres(ListCreateAPIView):
    queryset = ReceivedTyre.objects.all()
    serializer_class = ReceivedTyreSerializer


class AllReceivedSupplierTyres(ListCreateAPIView):
    queryset = ReceivedSupplierTyre.objects.all()
    serializer_class = ReceivedSupplierTyreSerializer


class ReceiveTyreListView(ListCreateAPIView):
    queryset = ReceivedTyre.objects.all()
    serializer_class = ReceivedTyreSerializer
    pagination_class = DefaultPagination


class ReceiveTyreListDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ReceivedTyre.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReceivedTyreSerializer
        return ReceivedTyreUpdateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        received_tyres = request.data.get('received_tyres')

        for received_tyre in received_tyres:
            try:
                received = ReceivedSupplierTyre.objects.get(
                    id=received_tyre['id'])
            except:
                send_supplier_tyre_id = received_tyre.pop('send_supplier_tyre')
                send_supplier_tyre_instance = SendSupplierTyre.objects.get(
                    id=send_supplier_tyre_id)
                ReceivedSupplierTyre.objects.create(
                    received_tyre=instance, send_supplier_tyre=send_supplier_tyre_instance, **received_tyre)

        return super().update(request, *args, **kwargs)

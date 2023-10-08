from rest_framework import serializers
from dag_section_data.models import TakenTyre, CustomerTakenTyre
from dag_section_data.models import SendTyre, SendSupplierTyre, ReceivedTyre, ReceivedSupplierTyre
from report_data.models import RebuildReport

# takenTyre
class CustomerTakenTyreSerializer(serializers.ModelSerializer):
    tyre_taken = serializers.CharField(read_only=True)

    class Meta:
        model = CustomerTakenTyre
        fields = ['rebuild_id', 'tyre_taken', 'tyre_no', 'size', 'brand']


class TakenTyreCreateSerializer(serializers.ModelSerializer):
    customer_tyres = CustomerTakenTyreSerializer(many=True)

    class Meta:
        model = TakenTyre
        fields = ['id', 'customer', 'vehicle', 'taken_date', 'customer_tyres']

    def create(self, validated_data):
        customer_tyres = validated_data.pop("customer_tyres")
        tyre_taken = TakenTyre.objects.create(**validated_data)

        for customer_tyre in customer_tyres:
            customer_taken_tyre = CustomerTakenTyre.objects.create(tyre_taken=tyre_taken, **customer_tyre)

            ## Report             
            RebuildReport.objects.create(
                rebuild_id=customer_taken_tyre, 
                customer_id=tyre_taken.customer.id,
                vehicle_id=tyre_taken.vehicle.vehical_no,
                taken_date=tyre_taken.taken_date,
                tyre_no=customer_taken_tyre.tyre_no,
                size=customer_taken_tyre.size,
                brand=customer_taken_tyre.brand
                )
            
        return tyre_taken


class TakenTyreUpdateSerializer(serializers.ModelSerializer):
    customer_tyres = CustomerTakenTyreSerializer(many=True, read_only=True)

    class Meta:
        model = TakenTyre
        fields = ['id', 'customer', 'vehicle', 'taken_date', 'customer_tyres']


# Send Tyre
class SendSupplierTyreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendSupplierTyre
        fields = ['id', 'job_no', 'customer_taken_tyre', 'status']


class SendTyreCreateSerializer(serializers.ModelSerializer):
    send_tyres = SendSupplierTyreSerializer(many=True)

    class Meta:
        model = SendTyre
        fields = ['order_no', 'supplier', 'taken_date', 'send_tyres']

    def create(self, validated_data):
        supplier_tyres = validated_data.pop('send_tyres')
        send_tyre = SendTyre.objects.create(**validated_data)

        for tyre in supplier_tyres:
            send_supplier_tyre = SendSupplierTyre.objects.create(send_tyre=send_tyre, **tyre)
          
            ### Report
            try:
                rebuild_report = RebuildReport.objects.get(rebuild_id_id=send_supplier_tyre.customer_taken_tyre.rebuild_id)              
                rebuild_report.supplier = send_tyre.supplier
                rebuild_report.send_date = send_tyre.taken_date
                rebuild_report.order_no = send_tyre.order_no
                rebuild_report.job_no = send_supplier_tyre.job_no
                rebuild_report.status = send_supplier_tyre.status
                rebuild_report.save()
            except:
                pass
            
            
        return send_tyre


class SendTyreUpdateSerializer(serializers.ModelSerializer):
    send_tyres = SendSupplierTyreSerializer(many=True, read_only=True)

    class Meta:
        model = SendTyre
        fields = ['order_no', 'supplier', 'taken_date', 'send_tyres']


# Received Tyres
class ReceivedSupplierTyreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedSupplierTyre
        fields = ['id', 'cost', 'status', 'send_supplier_tyre']


class ReceivedTyreSerializer(serializers.ModelSerializer):
    received_tyres = ReceivedSupplierTyreSerializer(many=True)

    class Meta:
        model = ReceivedTyre
        fields = ['invoice_no', 'date', 'received_tyres']

    def create(self, validated_data):
        received_tyres = validated_data.pop('received_tyres')
        insatnce = ReceivedTyre.objects.create(**validated_data)

        for received_tyre in received_tyres:
            received_supplier_tyre = ReceivedSupplierTyre.objects.create(received_tyre=insatnce, **received_tyre)

            try:
                send_supplier_tyre = SendSupplierTyre.objects.get(job_no=received_supplier_tyre.send_supplier_tyre)                
                rebuild_report = RebuildReport.objects.get(rebuild_id_id=send_supplier_tyre.customer_taken_tyre.rebuild_id)    
                rebuild_report.received_date = insatnce.date            
                rebuild_report.status = received_supplier_tyre.status
                rebuild_report.cost = received_supplier_tyre.cost
                rebuild_report.save()
            except:
                pass
        return insatnce


class ReceivedTyreUpdateSerializer(serializers.ModelSerializer):
    received_tyres = ReceivedSupplierTyreSerializer(many=True, read_only=True)

    class Meta:
        model = ReceivedTyre
        fields = ['invoice_no', 'date', 'received_tyres']

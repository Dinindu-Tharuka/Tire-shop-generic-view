from rest_framework import serializers
from dag_section_data.models import TakenTyre, CustomerTakenTyre
from dag_section_data.models import SendTyre, SendSupplierTyre, ReceivedTyre, ReceivedSupplierTyre

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
        print(validated_data)
        customer_tyres = validated_data.pop("customer_tyres")
        tyre_taken = TakenTyre.objects.create(**validated_data)

        for customer_tyre in customer_tyres:
            CustomerTakenTyre.objects.create(
                tyre_taken=tyre_taken, **customer_tyre)

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
            SendSupplierTyre.objects.create(send_tyre=send_tyre, **tyre)
        return send_tyre


class SendTyreUpdateSerializer(serializers.ModelSerializer):
    send_tyres = SendSupplierTyreSerializer(many=True, read_only=True)

    class Meta:
        model = SendTyre
        fields = ['order_no', 'supplier', 'taken_date', 'send_tyres']


## Received Tyres
class ReceivedSupplierTyreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedSupplierTyre
        fields = ['id', 'cost', 'status', 'send_supplier_tyre']

class ReceivedTyreSerializer(serializers.ModelSerializer):
    received_tyres= ReceivedSupplierTyreSerializer(many=True)
    class Meta:
        model = ReceivedTyre
        fields = ['invoice_no', 'date', 'received_tyres']

    def create(self, validated_data):
        received_tyres = validated_data.pop('received_tyres')
        insatnce = ReceivedTyre.objects.create(**validated_data)

        for received_tyre in received_tyres:
            ReceivedSupplierTyre.objects.create(received_tyre=insatnce, **received_tyre)
        return insatnce
    
class ReceivedTyreUpdateSerializer(serializers.ModelSerializer):
    received_tyres = ReceivedSupplierTyreSerializer(many=True, read_only=True)
    class Meta:
        model = ReceivedTyre
        fields = ['invoice_no', 'date', 'received_tyres']
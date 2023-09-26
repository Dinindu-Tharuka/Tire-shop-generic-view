from rest_framework import serializers
from dag_section_data.models import TakenTyre, CustomerTakenTyre
from dag_section_data.models import SendTyre, SendSupplierTyre

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
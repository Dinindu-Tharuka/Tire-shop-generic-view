from rest_framework import serializers
from dag_section_data.models import TakenTyre, CustomerTakenTyre

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


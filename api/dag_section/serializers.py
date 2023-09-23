from rest_framework import serializers
from dag_section_data.models import TakenTyre, CustomerTakenTyre

## takenTyre
class TakenTyreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakenTyre
        fields = ['id', 'customer', 'vehicle', 'taken_date']

class CustomerTakenTyreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerTakenTyre
        fields = ['rebuild_id', 'tyre_taken', 'tyre_no', 'size', 'brand']
from rest_framework import serializers
from report_data.models import RebuildReport

class RebuildReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = RebuildReport
        fields = ['rebuild_id', 'customer', 'vehicle', 'taken_date', 'tyre_no', 'size', 'brand', 'supplier', 'send_date', 'order_no', 'job_no', 'received_date', 'status', 'invoice_date', 'cost']

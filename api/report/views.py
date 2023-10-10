from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from report_data.models import RebuildReport
from .serializers import RebuildReportSerializer
from api.paginations import DefaultPagination

class RebuildReportListView(ListCreateAPIView):
    queryset = RebuildReport.objects.all()
    serializer_class = RebuildReportSerializer

class RebuildReportPageListView(ListCreateAPIView):
    serializer_class = RebuildReportSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        pageReportsRebuildIdFilter = self.request.GET.get('pageReportsRebuildIdFilter')
        pageReportsJobNoFilter = self.request.GET.get('pageReportsJobNoFilter')
        pageReportsCustomerFilter = self.request.GET.get('pageReportsCustomerFilter')
        pageReportVehicleFilter = self.request.GET.get('pageReportVehicleFilter')


        if pageReportsRebuildIdFilter or pageReportsJobNoFilter or pageReportsCustomerFilter or pageReportVehicleFilter:            
           
            queryset = RebuildReport.objects\
                        .filter(rebuild_id__rebuild_id__istartswith=pageReportsRebuildIdFilter)\
                        .filter(job_no__istartswith=pageReportsJobNoFilter)
            
            if pageReportsCustomerFilter:
                queryset = queryset.filter(customer__id = pageReportsCustomerFilter)

            if pageReportVehicleFilter:
                queryset = queryset.filter(vehicle__vehical_no = pageReportVehicleFilter)                   
        else:
            queryset = RebuildReport.objects.all()
        return queryset

class RebuildReportDetailView(RetrieveUpdateDestroyAPIView):
    queryset = RebuildReport.objects.all()
    serializer_class = RebuildReportSerializer


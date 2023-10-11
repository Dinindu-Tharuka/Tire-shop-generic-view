from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from report_data.models import RebuildReport
from .serializers import RebuildReportSerializer
from api.paginations import DefaultPagination

class RebuildReportListView(ListCreateAPIView):
    queryset = RebuildReport.objects.all()
    serializer_class = RebuildReportSerializer

    def get_queryset(self):
        reportsRebuildIdFilter = self.request.GET.get('reportsRebuildIdFilter')
        reportsJobNoFilter = self.request.GET.get('reportsJobNoFilter')
        reportsCustomerFilter = self.request.GET.get('reportsCustomerFilter')
        reportVehicleFilter = self.request.GET.get('reportVehicleFilter')
        
        if reportsRebuildIdFilter or reportsJobNoFilter or reportsCustomerFilter or reportVehicleFilter:            
           
            queryset = RebuildReport.objects.order_by('-taken_date').all()
                        
            if reportsJobNoFilter:
                queryset = queryset.filter(job_no__istartswith=reportsJobNoFilter)
            
            if reportsRebuildIdFilter:
                queryset = queryset.filter(rebuild_id__rebuild_id__istartswith=reportsRebuildIdFilter)
            
            if reportsCustomerFilter:
                queryset = queryset.filter(customer__id = reportsCustomerFilter)

            if reportVehicleFilter:
                queryset = queryset.filter(vehicle__vehical_no = reportVehicleFilter)                   
        else:
            queryset = RebuildReport.objects.order_by('-taken_date').all()
        return queryset

class RebuildReportPageListView(ListCreateAPIView):
    serializer_class = RebuildReportSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        pageReportsRebuildIdFilter = self.request.GET.get('pageReportsRebuildIdFilter')
        pageReportsJobNoFilter = self.request.GET.get('pageReportsJobNoFilter')
        pageReportsCustomerFilter = self.request.GET.get('pageReportsCustomerFilter')
        pageReportVehicleFilter = self.request.GET.get('pageReportVehicleFilter')


        if pageReportsRebuildIdFilter or pageReportsJobNoFilter or pageReportsCustomerFilter or pageReportVehicleFilter:            
           
            queryset = RebuildReport.objects.order_by('-taken_date').all()
                        
            if pageReportsJobNoFilter:
                queryset = queryset.filter(job_no__istartswith=pageReportsJobNoFilter)
            
            if pageReportsRebuildIdFilter:
                queryset = queryset.filter(rebuild_id__rebuild_id__istartswith=pageReportsRebuildIdFilter)
            
            if pageReportsCustomerFilter:
                queryset = queryset.filter(customer__id = pageReportsCustomerFilter)

            if pageReportVehicleFilter:
                queryset = queryset.filter(vehicle__vehical_no = pageReportVehicleFilter)                   
        else:
            queryset = RebuildReport.objects.order_by('-taken_date').all()
        return queryset

class RebuildReportDetailView(RetrieveUpdateDestroyAPIView):
    queryset = RebuildReport.objects.all()
    serializer_class = RebuildReportSerializer


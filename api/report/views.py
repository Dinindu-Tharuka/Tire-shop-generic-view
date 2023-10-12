from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from report_data.models import RebuildReport
from .serializers import RebuildReportSerializer
from api.paginations import DefaultPagination
import datetime

class ConvertDateToDateTime:
    def __init__(self, date_start=None, date_end=None):
        self.date_start = date_start
        self.date_end = date_end

        if self.date_end and self.date_start:
            date_object_start = datetime.datetime.strptime(self.date_start, "%Y-%m-%d").date()
            date_object_end = datetime.datetime.strptime(self.date_end, "%Y-%m-%d").date()
            self.today_min = datetime.datetime.combine(date_object_start, datetime.time.min)
            self.today_max = datetime.datetime.combine(date_object_end, datetime.time.max)
        elif self.date_start:
            date_object = datetime.datetime.strptime(self.date_start, "%Y-%m-%d").date()
            self.today_min = datetime.datetime.combine(date_object, datetime.time.min)
            self.today_max = datetime.datetime.combine(date_object, datetime.time.max)

    def converted_min(self):
        return self.today_min
    
    def converted_max(self):
        return self.today_max
        
            


class RebuildReportListView(ListCreateAPIView):
    queryset = RebuildReport.objects.all()
    serializer_class = RebuildReportSerializer

    def get_queryset(self):
        reportsRebuildIdFilter = self.request.GET.get('reportsRebuildIdFilter')
        reportsJobNoFilter = self.request.GET.get('reportsJobNoFilter')
        reportsCustomerFilter = self.request.GET.get('reportsCustomerFilter')
        reportVehicleFilter = self.request.GET.get('reportVehicleFilter')
        reportStartDateFilter = self.request.GET.get('reportStartDateFilter')
        reportEndDateFilter = self.request.GET.get('reportEndDateFilter')

        

        print('reportStartDateFilter', reportStartDateFilter)
        
        if reportsRebuildIdFilter or reportsJobNoFilter or reportsCustomerFilter or reportVehicleFilter or reportStartDateFilter or reportEndDateFilter:            
           
            queryset = RebuildReport.objects.order_by('-taken_date').all()
                        
            if reportsJobNoFilter:
                queryset = queryset.filter(job_no__istartswith=reportsJobNoFilter)
            
            if reportsRebuildIdFilter:
                queryset = queryset.filter(rebuild_id__rebuild_id__istartswith=reportsRebuildIdFilter)
            
            if reportsCustomerFilter:
                queryset = queryset.filter(customer__id = reportsCustomerFilter)

            if reportVehicleFilter:
                queryset = queryset.filter(vehicle__vehical_no = reportVehicleFilter) 

            if reportStartDateFilter or reportEndDateFilter:

                date_time = ConvertDateToDateTime(reportStartDateFilter, reportEndDateFilter)

                print('converted', date_time.converted_min())
                print('converted', date_time.converted_max())
                
                
                if reportStartDateFilter and reportEndDateFilter:
                    queryset = queryset.filter(taken_date__range=(reportStartDateFilter, reportEndDateFilter))
                elif reportStartDateFilter:
                    queryset = queryset.filter(taken_date__range = (date_time.converted_min(), date_time.converted_max()) )
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
        pageReportStartDateFilter = self.request.GET.get('pageReportStartDateFilter')
        pageReportEndDateFilter = self.request.GET.get('pageReportEndDateFilter')

        


        if pageReportsRebuildIdFilter or pageReportsJobNoFilter or pageReportsCustomerFilter or pageReportVehicleFilter or pageReportStartDateFilter or pageReportEndDateFilter:            
           
            queryset = RebuildReport.objects.order_by('-taken_date').all()
                        
            if pageReportsJobNoFilter:
                queryset = queryset.filter(job_no__istartswith=pageReportsJobNoFilter)
            
            if pageReportsRebuildIdFilter:
                queryset = queryset.filter(rebuild_id__rebuild_id__istartswith=pageReportsRebuildIdFilter)
            
            if pageReportsCustomerFilter:
                queryset = queryset.filter(customer__id = pageReportsCustomerFilter)

            if pageReportVehicleFilter:
                queryset = queryset.filter(vehicle__vehical_no = pageReportVehicleFilter)  

            if pageReportStartDateFilter or pageReportEndDateFilter: 
                date_time = ConvertDateToDateTime(pageReportStartDateFilter, pageReportEndDateFilter)

                print('converted', type(date_time.converted_min()))
                print('converted', date_time.converted_max())

                if pageReportStartDateFilter and pageReportEndDateFilter:
                    queryset = queryset.filter(taken_date__range=(pageReportStartDateFilter, pageReportEndDateFilter))
                elif pageReportStartDateFilter:                    
                    queryset = queryset.filter(taken_date__range = (date_time.converted_min(), date_time.converted_max()))
        else:
            queryset = RebuildReport.objects.order_by('-taken_date').all()
        return queryset

class RebuildReportDetailView(RetrieveUpdateDestroyAPIView):
    queryset = RebuildReport.objects.all()
    serializer_class = RebuildReportSerializer


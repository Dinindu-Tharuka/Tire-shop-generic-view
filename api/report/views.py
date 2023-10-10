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
        if pageReportsRebuildIdFilter or pageReportsJobNoFilter:
            queryset = RebuildReport.objects\
                        .filter(rebuild_id__rebuild_id__istartswith=pageReportsRebuildIdFilter)\
                        .filter(job_no__istartswith=pageReportsJobNoFilter)
        else:
            queryset = RebuildReport.objects.all()
        return queryset

class RebuildReportDetailView(RetrieveUpdateDestroyAPIView):
    queryset = RebuildReport.objects.all()
    serializer_class = RebuildReportSerializer


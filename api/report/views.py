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
        if pageReportsRebuildIdFilter:
            queryset = RebuildReport.objects.filter(rebuild_id__rebuild_id__istartswith=pageReportsRebuildIdFilter) 
        else:
            queryset = RebuildReport.objects.all()
        return queryset

class RebuildReportDetailView(RetrieveUpdateDestroyAPIView):
    queryset = RebuildReport.objects.all()
    serializer_class = RebuildReportSerializer


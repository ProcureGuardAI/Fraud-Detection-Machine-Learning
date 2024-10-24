from rest_framework import viewsets
from .models import Report
from .serializers import ReportSerializer
# Create your views here.

class ReportListView(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

from rest_framework.viewsets import ModelViewSet
from .serializers import PostReportSerializer
from .models import PostReport


class PostReportModelViewset(ModelViewSet):
    queryset = PostReport.objects.all()
    serializer_class = PostReportSerializer

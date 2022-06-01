from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from .serializers import PostReportSerializer
from .models import PostReport


class PostDetailAPI(generics.RetrieveAPIView):
    queryset = PostReport.objects.all()
    serializer_class = PostReportSerializer
    lookup_field = 'slug'


class PostReportModelViewset(ModelViewSet):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAuthenticated()]
    queryset = PostReport.objects.all()
    serializer_class = PostReportSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        elif self.action == 'retrieve':
            return [AllowAny()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == 'update':
            return [IsAuthenticated()]
        elif self.action == 'partial_update':
            return [IsAuthenticated()]
        elif self.action == 'destroy':
            return [IsAuthenticated()]
        else:
            return super(PostReportModelViewset, self).get_permissions()
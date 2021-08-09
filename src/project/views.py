  
from django.db.models import Q
from rest_framework.generics import (CreateAPIView, ListAPIView,RetrieveAPIView)
from rest_framework.permissions import (IsAuthenticated,AllowAny)

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from .models import Project
from .serializer import (ProjectCreateUpdateSerializer, ProjectDetailSerializer,ProjectListSerializer)

# Create your views here.
class ProjectCreateAPIView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class ProjectListAPIView(ListAPIView):
    serializer_class = ProjectListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['title']
    #pagination_class = PostPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Project.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query)
                    ).distinct()
        return queryset_list




class ProjectDetailAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
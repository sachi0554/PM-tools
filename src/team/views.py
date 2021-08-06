from django.db.models import Q
from rest_framework.generics import (CreateAPIView, RetrieveAPIView)
from rest_framework.permissions import (IsAuthenticated,AllowAny)

from .models import (Team,Member)
from .serializer import (TeamCreateUpdateSerializer,TeamPlayerCreateUpdateSerializer,TeamDetailSerializer)

# Create your views here.


class TeamCreateAPIView(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TeamPlayerCreateAPIView(CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = TeamPlayerCreateUpdateSerializer
    permission_classes = [IsAuthenticated]



class TeamDetailAPIView(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
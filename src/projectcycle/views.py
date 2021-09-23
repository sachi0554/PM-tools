from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, RetrieveAPIView)
from rest_framework.permissions import (IsAuthenticated)
from .serializer import ProjectCycleDetailSerializer
from .models import ProjectCycle
# Create your views here.
class CyclereateAPIView(CreateAPIView):
    queryset = ProjectCycle.objects.all()
    serializer_class = ProjectCycleDetailSerializer
    permission_classes = [IsAuthenticated]

    
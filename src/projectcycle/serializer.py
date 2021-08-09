
from rest_framework.serializers import ModelSerializer
from .models import ProjectCycle

class ProjectCycleDetailSerializer(ModelSerializer):  
    class Meta:
        model = ProjectCycle
        fields = '__all__'
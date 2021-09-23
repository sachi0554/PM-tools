
  
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from .models import Project

from team.models import Team
from team.serializer import TeamDetailSerializer
from projectcycle.models import ProjectCycle
from projectcycle.serializer import ProjectCycleDetailSerializer

class ProjectCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



class ProjectListSerializer(ModelSerializer):
    #user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Project
        fields = '__all__'



class ProjectDetailSerializer(ModelSerializer): 
    team = SerializerMethodField()
    projectcycle = SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'

    def get_projectcycle(self, obj):
        c_qs = ProjectCycle.objects.filter_by_instance(obj)
        projectcycle = ProjectCycleDetailSerializer(c_qs, many=True).data
        return projectcycle

    def get_team(self, obj):
        c_qs = Team.objects.filter_by_instance(obj)
        team = TeamDetailSerializer(c_qs, many=True).data
        return team







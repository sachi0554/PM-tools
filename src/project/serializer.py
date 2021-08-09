
  
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from .models import Project
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
    projectcycle = SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'

    def get_projectcycle(self, obj):
        c_qs = ProjectCycle.objects.filter_by_instance(obj)
        projectcycle = ProjectCycleDetailSerializer(c_qs, many=True).data
        return projectcycle







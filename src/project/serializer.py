
  
from rest_framework.serializers import ModelSerializer
from .models import Project

class ProjectCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



class ProjectListSerializer(ModelSerializer):
    #user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Project
        fields = '__all__'







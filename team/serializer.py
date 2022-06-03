  
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import (Team,Member)


class TeamCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamPlayerCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class TeamDetailSerializer(ModelSerializer):
 
   # user = UserDetailSerializer(read_only=True)
 
    member = SerializerMethodField()
    class Meta:
        model = Team
        fields = '__all__'

    def get_member(self, obj):
        c_qs = Member.objects.filter_by_instance(obj)
        members = MemberDetailSerializer(c_qs, many=True).data
        return members


class MemberDetailSerializer(ModelSerializer):  
    class Meta:
        model = Member
        fields = '__all__'

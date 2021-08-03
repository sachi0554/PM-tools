from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model



from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError
    )


User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return data

   
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
                username = username,
                email = email
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(label='Email Address' , required=True , allow_blank=False)
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'token',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        user_obj= None
        email = data.get("email")
        password = data["password"]
        if not email :
            raise ValidationError("A email must required")
        
        user = User.objects.filter(
                Q(email=email)
            ).distinct()

        if user.exists() and user.count() == 1 :
            user_obj = user.first()
        else:
            raise ValidationError("email and password must be provided")
        
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("user not valid user")
        
        data["token"] = "temprory token"
        return data

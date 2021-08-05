from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework_jwt.settings import api_settings
import jwt


from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError
    )


User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    name = CharField(max_length=255)
    email = EmailField(label='Email Address')
    confirm_password =CharField(
        write_only=True,
        required=True,
        label="re-password"
    )

    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'password',
            'confirm_password'
            
        ]
        extra_kwargs = {"confirm_password":
                            {"write_only": True},
                            "password":
                            {"write_only": True}
                            }
    

    def validate_email(self, email):
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return email
    

    def validate(self, data):
        print(data)
        if not data['password'] or not data['confirm_password']:
            raise ValidationError("Please enter a password and confirm it.")
        if data['password'] != data['confirm_password']:
            raise ValidationError("Those passwords don't match.")
        return data

   
    def create(self, validated_data):
        email = validated_data['email']
        name= validated_data['name']
        password = validated_data['confirm_password']
        user_obj = User(
                email = email,
                name= name
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

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)

        data["token"] = token
        return data

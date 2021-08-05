from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token


from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    )

urlpatterns = [
    url('register', UserCreateAPIView.as_view(), name='register'),
    url('login', UserLoginAPIView.as_view(), name='login'),
    url(r'^token', obtain_jwt_token),
    url(r'^refresh-token', refresh_jwt_token),
]
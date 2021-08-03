from django.conf.urls import url


from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    )

urlpatterns = [
    url('register', UserCreateAPIView.as_view(), name='register'),
    url('login', UserLoginAPIView.as_view(), name='login')
]
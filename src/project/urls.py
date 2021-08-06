
 
from django.conf.urls import url
from .views import (ProjectCreateAPIView,ProjectListAPIView)


urlpatterns = [
    url(r'^create', ProjectCreateAPIView.as_view(), name="create"),
    url(r'^list', ProjectListAPIView.as_view(), name="list"),
]

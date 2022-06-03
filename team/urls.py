
 
from django.conf.urls import url
from .views import (TeamCreateAPIView,TeamPlayerCreateAPIView, TeamDetailAPIView)


urlpatterns = [
    url(r'^create', TeamCreateAPIView.as_view(), name="createteam"),
    url(r'^addmember', TeamPlayerCreateAPIView.as_view(), name="member"),
    url(r'^(?P<id>[\w-]+)/$', TeamDetailAPIView.as_view(), name='detail'),
]


 
from django.conf.urls import url
from .views import (CyclereateAPIView)


urlpatterns = [
      
    url(r'^create', CyclereateAPIView.as_view(), name="create"),
    
]


from community.api.views import communityListAPIView
from django.urls import path, include

urlpatterns = [
    path('list/', communityListAPIView.as_view(), name = 'list')
] 
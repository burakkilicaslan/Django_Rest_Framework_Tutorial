
from django.urls import path, include
from myblog.community.api.views import communityListAPIView

urlpatterns = [
    path('list/', communityListAPIView.as_view(), name = 'list')
]
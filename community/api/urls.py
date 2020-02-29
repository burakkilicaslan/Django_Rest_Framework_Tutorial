
from community.api.views import communityListAPIView, communitydetailAPIView, communitydeleteAPIView, communityupdateAPIView
from django.urls import path, include

urlpatterns = [
    path('list/', communityListAPIView.as_view(), name = 'list'),
    path('detail/<pk>', communitydetailAPIView.as_view(), name = 'detail'),
    path('update/<pk>', communityupdateAPIView.as_view(), name='update'),
    path('delete/<pk>', communitydeleteAPIView.as_view(), name='delete')

] 
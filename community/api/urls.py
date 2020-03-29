from community.api import views
from community.api.views import (communityListAPIView,
                                 communitydetailAPIView,
                                 communitydeleteAPIView,
                                 communityupdateAPIView,
                                 communitycreateAPIView,
                                 action_list)
from django.urls import path, include

urlpatterns = [
    path('list/', communityListAPIView.as_view(), name = 'list'),
    path('detail/<slug>', communitydetailAPIView.as_view(), name = 'detail'),
    path('update/<pk>', communityupdateAPIView.as_view(), name='update'),
    path('delete/<pk>', communitydeleteAPIView.as_view(), name='delete'),
    path('create/', communitycreateAPIView.as_view(), name='create'),
    path('actions/', views.action_list),

]
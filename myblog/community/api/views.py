from rest_framework.generics import ListAPIView

from myblog.community.api.serializers import communityserializer
from myblog.community.models import communities

class communityListAPIView(ListAPIView):

    queryset = communities.objects.all()

    def get_queryset(self):
        community_list = communities.objects.order_by("creation_date")
        serializer_class = communityserializer
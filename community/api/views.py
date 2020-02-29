from rest_framework.generics import ListAPIView

from community.api.serializers import communityserializer
from community.models import communities

class communityListAPIView(ListAPIView):

    queryset = communities.objects.all()
    serializer_class = communityserializer

    def get_queryset(self):
        community_list = communities.objects.order_by("creation_date")

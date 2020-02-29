from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from community.api.serializers import communityserializer
from community.models import communities


class communityListAPIView(ListAPIView):
    queryset = communities.objects.all()
    serializer_class = communityserializer

    # def get_queryset(self):
    #    community_list = communities.objects.order_by("creation_date")


class communitydetailAPIView(RetrieveAPIView):
    queryset = communities.objects.all()
    serializer_class = communityserializer
    lookup_field = 'pk'


class communityupdateAPIView(UpdateAPIView):
    queryset = communities.objects.all()
    serializer_class = communityserializer
    lookup_field = 'pk'


class communitydeleteAPIView(DestroyAPIView):
    queryset = communities.objects.all()
    serializer_class = communityserializer
    lookup_field = 'pk'

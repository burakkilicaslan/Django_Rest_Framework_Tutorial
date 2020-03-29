from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     CreateAPIView)
from rest_framework.parsers import JSONParser

from community.api.serializers import communityserializer, actionserializer, post_typeserializer
from community.models import communities, post_type
from actstream import action
from actstream.models import action_object_stream
from django.db.models.signals import post_save



class communityListAPIView(ListAPIView):
    queryset = communities.objects.all()
    serializer_class = communityserializer

    # def get_queryset(self):
    #    community_list = communities.objects.order_by("creation_date")


class communitydetailAPIView(RetrieveAPIView):
    queryset = communities.objects.all()
    serializer_class = communityserializer
    lookup_field = 'slug'


class communityupdateAPIView(UpdateAPIView):
    queryset = communities.objects.all()
    serializer_class = communityserializer
    lookup_field = 'pk'


class communitydeleteAPIView(DestroyAPIView):
    queryset = communities.objects.all()
    serializer_class = communityserializer
    lookup_field = 'pk'

class communitycreateAPIView(CreateAPIView):
    queryset = communities.objects.all()
    serializer_class = communityserializer

class post_typecreateAPIView(CreateAPIView):
    queryset = post_type.objects.all()
    serializer_class = post_typeserializer


@csrf_exempt
def action_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        #actions = action_object_stream.objects.all()
        serializer = actionserializer
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = actionserializer(data=data)
        if serializer.is_valid():
            posts = post_type.objects.get(id = postid)
            community = communities.objects.get(id=communityid)
            action.send(posts, verb='posted', target = community)
            return JsonResponse(serializer.data, status=201)


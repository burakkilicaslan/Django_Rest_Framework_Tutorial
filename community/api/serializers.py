from rest_framework import serializers


class communityserializer(serializers.Serializer):

    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)

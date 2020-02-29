from rest_framework import serializers

from community.models import communities


### This is serializer method that you can define every field manually.

# class communityserializer(serializers.Serializer):
#
#     name = serializers.CharField(max_length=200)
#     description = serializers.CharField(max_length=200)
#     user = serializers.CharField(max_length=200)
#     creation_date = serializers.DateTimeField()



### this is model serializer which field definitions are more easy.

class communityserializer(serializers.ModelSerializer):

    #user = serializers.CharField(max_length=200)

    class Meta:
        model = communities
        fields = [
            'name',
            'description',
            'creation_date',
            'modification_date',
            'image',
            'slug'
        ]
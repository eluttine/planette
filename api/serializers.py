from rest_framework import serializers

from planet.models import Post


class PostSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)


    class Meta:
        model = Post
        fields = ('id', 'title', 'url', 'date_modified', 'thumbnail', 'authors')

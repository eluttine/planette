from rest_framework import serializers

from planet.models import Post


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    url = serializers.URLField(max_length=1000)


class FeedSerializer(serializers.Serializer):
    blog = BlogSerializer()


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    title = serializers.CharField(max_length=255)
    url = serializers.URLField(max_length=1000)
    date_modified = serializers.DateTimeField(allow_null=True, required=False)
    thumbnail = serializers.ImageField(allow_null=True, required=False)
    authors = serializers.StringRelatedField(many=True)
    feed = FeedSerializer()

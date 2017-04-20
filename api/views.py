from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from planet.models import Post
from api.serializers import PostSerializer

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all().order_by('-date_modified')[:30]
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

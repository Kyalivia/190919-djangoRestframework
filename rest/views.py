from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets

# CBV
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


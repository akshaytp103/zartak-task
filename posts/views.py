from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from user_profile.permissions import IsOwnerOrReadOnly
from rest_framework import serializers, viewsets,status,permissions
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404

class PostViewSet(viewsets.ViewSet):
    """
    Posts
    """
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(user)
        return Response(serializer.data)
    
    
class AddPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer   
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,IsAdminUser]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
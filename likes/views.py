from posts.models import Post
from .permissions import hasSelfLikedOrReadOnly
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, viewsets,status,permissions
from . models import Like
from . serializers import LikeSerializer



# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset=Like.objects.all()
    serializer_class=LikeSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,hasSelfLikedOrReadOnly]
    def perform_create(self,serializer):
        post_instance=get_object_or_404(Post,pk=self.request.data['post'])

        #if user likes the post
        if self.request.data['up_like']:
            already_liked_by=Like.objects.filter(post=post_instance,liked_by=self.request.user).exists()
            if already_liked_by:
                raise serializers.ValidationError({"message":"You have already liked this post"})
            else:
                serializer.save(liked_by=self.request.user,post=post_instance)
        #if dislikes
        else:
            already_disliked_by=Like.objects.filter(post=post_instance,disliked_by=self.request.user).exists()
            if already_disliked_by:
                raise serializers.ValidationError({"message":"You have already disliked this post"})
            else    :
                serializer.save(dislike_by=self.request.user,post=post_instance)
                
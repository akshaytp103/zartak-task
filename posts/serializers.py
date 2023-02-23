from .models import Post
from rest_framework import serializers

from likes.serializers import LikeSerializer


class PostSerializer(serializers.ModelSerializer):
   
    likes=LikeSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'content','post_image','category','post_date','likes']
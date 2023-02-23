from .models import Like
from rest_framework import serializers

class LikeSerializer(serializers.ModelSerializer):
    liked_by = serializers.ReadOnlyField(source='liked_by.username')
    disliked_by=serializers.ReadOnlyField(source='disliked_by.username')
    class Meta:
        model = Like
        fields = ['id','post','liked_by','disliked_by']
        
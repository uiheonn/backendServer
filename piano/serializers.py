from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Post

class PostSerializer(ModelSerializer):
    auth_username = ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['id', 'auth_username', 'message']
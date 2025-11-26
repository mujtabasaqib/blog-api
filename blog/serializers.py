from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id','title','slug','author','author_username','body','status','created','updated']
        read_only_fields = ['author','created','updated','author_username']


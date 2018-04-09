from rest_framework import serializers

from wall.models import Post

class PostSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Post
        fields = '__all__'

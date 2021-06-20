from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=20)
    content = serializers.CharField(max_length=100)
    created_by = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.save()
        return instance

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_by']






from rest_framework import serializers
from .models import PostModel, TopicModel, ThreadModel


class PostSerializer(serializers.Serializer):
    post = serializers.CharField(max_length=1000)
    thread = serializers.IntegerField()
    user = serializers.IntegerField()


class ThreadSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    topic = serializers.IntegerField()
    user = serializers.IntegerField()


class TopicSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)

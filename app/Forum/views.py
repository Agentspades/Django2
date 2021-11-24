from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer, ThreadSerializer, TopicSerializer
from .models import PostModel, TopicModel, ThreadModel
from Auth.models import User
# Create your views here.


class NewThread(APIView):
    serializer_class = ThreadSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            title = serializer.data.get('title')
            topicID = serializer.data.get('topic')
            userID = serializer.data.get('user')
            try:
                user = User.objects.get(id=userID)
                topic = TopicModel.objects.get(id=topicID)
                thread = ThreadModel(title=title, topicID=topic, userID=user)
                thread.save()
                message = f'A thread was created user: {user}, title: {title}, topic: {topic}'
                return Response({'message': message}, status=status.HTTP_200_OK)
            except:
                message = f'There was an error creating the thread'
                return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewPost(APIView):
    serializer_class = PostSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            post = serializer.data.get('post')
            threadID = serializer.data.get('thread')
            userID = serializer.data.get('user')
            try:
                user = User.objects.get(id=userID)
                thread = ThreadModel.objects.get(id=threadID)
                new_post = PostModel(post=post, threadID=thread, userID=user)
                new_post.save()
                message = f'A thread was created user: {user}, post: {post}, thread: {thread}'
                return Response({'message': message}, status=status.HTTP_200_OK)
            except:
                message = f'There was an error creating the post'
                return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

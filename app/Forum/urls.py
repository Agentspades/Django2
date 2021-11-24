from django.urls import path, include
from .views import NewThread, NewPost

urlpatterns = [
    path('forum/thread/new/', NewThread.as_view()),
    path('forum/post/new/', NewPost.as_view())
]

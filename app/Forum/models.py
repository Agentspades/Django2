from datetime import datetime
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class TopicModel(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        db_table = 'forum_topic'
        verbose_name_plural = "Forum Topics"

    def __str__(self):
        return self.title


class ThreadModel(models.Model):
    topicID = models.ForeignKey(
        'TopicModel', on_delete=CASCADE, db_column='topicID', default=0, verbose_name='Topic')
    userID = models.ForeignKey(
        'Auth.User', on_delete=CASCADE, db_column='userID', default=0, verbose_name='User')
    title = models.CharField(max_length=150)
    created = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'forum_thread'
        verbose_name_plural = 'Forum Threads'

    def __str__(self):
        return self.title


class PostModel(models.Model):
    threadID = models.ForeignKey(
        'ThreadModel', on_delete=CASCADE, db_column='threadID', default=0, verbose_name='Thread')
    userID = models.ForeignKey(
        'Auth.User', on_delete=CASCADE, db_column='userID', default=0, verbose_name='User')
    post = models.TextField()
    created = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'forum_post'
        verbose_name_plural = 'Forum Posts'

    def __str__(self):
        return self.post

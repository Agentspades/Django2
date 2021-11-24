from django.contrib import admin
from .models import TopicModel, ThreadModel, PostModel


class TopicModelAdmin(admin.ModelAdmin):
    list_display = ['title']


class ThreadModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['userID', 'created']


# Register your models here.
admin.site.register(TopicModel, TopicModelAdmin)
admin.site.register(ThreadModel, ThreadModelAdmin)
admin.site.register(PostModel, PostModelAdmin)

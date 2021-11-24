from django.contrib import admin
from Events import models
from django.contrib.auth.models import Group, User
from rest_framework.authtoken.models import TokenProxy

from .models import Event, EventRegistration


class EventAdmin(admin.ModelAdmin):
    search_fields = ['name']


class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ['eventID', 'userID', 'attendees']


# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)
admin.site.site_header = "Tafe APP Admin"

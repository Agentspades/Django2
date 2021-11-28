from rest_framework import serializers
from .models import EventRegistration, Event


class RegistrationList(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = '__all__'


class RegistrationSerializer(serializers.Serializer):
    # user = serializers.IntegerField(default=0)
    event = serializers.IntegerField(default=0)
    attendees = serializers.IntegerField(min_value=1, max_value=5)


class UpdateSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    event = serializers.IntegerField(default=0)
    attendees = serializers.IntegerField(min_value=1, max_value=5)


class EventList(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
